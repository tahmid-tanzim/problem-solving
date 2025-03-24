import argparse
import json
import os
import time
import traceback
import asyncio
from copy import deepcopy
from anthropic import AsyncAnthropic
import httpx
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import httpx
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from gpt4_context import EventParser
from src.asr.asr_replace import ASRReplace

app = Flask(__name__)
socketio = SocketIO(
    app, cors_allowed_origins="*"
)  # cors_allowed_origins is set to allow connections from any origin
parser = argparse.ArgumentParser()
parser.add_argument("--local", action="store_true")
parser.add_argument(
    "--restaurant-code",
    required=False,
    default="hardees_stevensville_gpt4_uat",
    help="the restaurant code from which items like menu, voiceprps are fetched from",
)
parser.add_argument(
    "--meal-periods",
    help='Active meal periods in preference order, IE "Breakfast,Lunch"',
)
parser.add_argument(
    "--environment",
    required=False,
    default="staging",
    help="events environment to use; staging by default",
)
parser.add_argument(
    "--brand",
    required=False,
    default="hardees_otac",
    help="Brand the restaurant code belongs to, Del Taco, Hardees, etc.",
)

args = parser.parse_args()
slack_client = WebClient(token=os.getenv("SLACK_TOKEN"))
ANTHROPIC_MODEL = "claude-3-5-sonnet-20241022"  # Using Claude model instead of OpenAI


# Load credentials from TOML file
def load_credentials_from_toml(file_path="credentials.toml"):
    """Load API credentials from a simple key-value file and set them as environment variables."""
    try:
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                if "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip('"')  # Remove quotes if present

                    # Set environment variable
                    os.environ[key] = value
                    print(f"Set environment variable: {key}")

        return True
    except Exception as e:
        print(f"Error loading credentials: {str(e)}")
        return False


# Try to load credentials from toml
credentials_file = os.path.join(os.path.dirname(__file__), "credentials.toml")
if os.path.exists(credentials_file):
    print(f"Loading credentials from {credentials_file}")
    load_credentials_from_toml(credentials_file)

    # Make ANTHROPIC_SDK_KEY available as ANTHROPIC_API_KEY
    if "ANTHROPIC_SDK_KEY" in os.environ and "ANTHROPIC_API_KEY" not in os.environ:
        os.environ["ANTHROPIC_API_KEY"] = os.environ["ANTHROPIC_SDK_KEY"]
        print("Set ANTHROPIC_API_KEY from ANTHROPIC_SDK_KEY")
else:
    print(f"Credentials file not found at {credentials_file}")
    # Try looking in parent directories
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    credentials_file = os.path.join(parent_dir, "credentials.toml")
    if os.path.exists(credentials_file):
        print(f"Loading credentials from {credentials_file}")
        load_credentials_from_toml(credentials_file)

        # Make ANTHROPIC_SDK_KEY available as ANTHROPIC_API_KEY
        if "ANTHROPIC_SDK_KEY" in os.environ and "ANTHROPIC_API_KEY" not in os.environ:
            os.environ["ANTHROPIC_API_KEY"] = os.environ["ANTHROPIC_SDK_KEY"]
            print("Set ANTHROPIC_API_KEY from ANTHROPIC_SDK_KEY")

EXPANDED_PROMPT_FILE = f"./configs/{args.brand}/prompts/fullmenu_reordered_expanded.txt"
event_parser = EventParser(
    prefer_ai_name=True,
    restaurant_code=args.restaurant_code,
    mock_rest_code=args.restaurant_code,
    environment=args.environment,
    brand=args.brand,
)
expand_slash_reply = event_parser.expand_slash_reply


def parse_cart(cart):
    event_parser.cart = cart
    return event_parser.parse_cart()


def print_prp_cart(cart):
    event_parser.get_prp_cart(cart, print_cart=True)


channel_transcript_map = {}  # Dictionary to store per-channel transcripts
channel_cost_map = {}  # Dictionary to store per-channel time&token cost

asr_replace = ASRReplace(args.brand)


def reset_transcript(channel_id):
    with open(event_parser.expanded_prompt_file, "r") as file:
        prompt = file.read()
    messages = [
        {"role": "system", "content": prompt},
        {"role": "assistant", "content": "AI: /greet\nCart:\n"},
    ]
    channel_transcript_map[channel_id] = messages
    channel_cost_map[channel_id] = {"input_tokens": 0, "output_tokens": 0, "time": 0}
    return messages


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/webpage/events", methods=["POST"])
def webpage_event():
    data = request.json  # or request.form, depending on how you're sending data
    message = data.get("message")
    channel_id = data.get("channel_id")  # or a default channel ID for webpage events

    # call your refactored message handling function
    response = {"transcript": handle_message(channel_id, message)}
    print("\n\n" + response["transcript"])

    return jsonify(response)


@app.route("/webpage/gettranscript", methods=["POST"])
def webpage_gettranscript():
    data = request.json  # or request.form, depending on how you're sending data
    channel_id = data.get("channel_id")  # or a default channel ID for webpage events
    transcript = stringify_transcript(channel_id)
    response = {"transcript": transcript}
    print("\n\n" + transcript)
    return jsonify(response)


@app.route("/slack/events", methods=["POST"])
def slack_event():
    if "x-amz-invocation-type" in request.headers:  # Check if running on AWS Lambda
        data = json.loads(request.data)
    else:
        data = request.json

    if "challenge" in data:
        return jsonify({"challenge": data["challenge"]})

    if "event" in data:
        slack_event = data["event"]
        if "text" in slack_event:
            message = slack_event["text"]
            channel_id = slack_event["channel"]

            handle_message(channel_id, message)

            try:
                slack_client.chat_postMessage(
                    channel=channel_id, text=stringify_transcript(channel_id)
                )
            except SlackApiError as e:
                print(f"Error sending message: {e.response['error']}")

    return jsonify({"status": "ok"})


@socketio.on("connect")
def test_connect():
    print("Client connected")
    handle_message("llm-bot", "\\reset")


@socketio.on("my event")
def handle_my_custom_event(json):
    print(json)
    message = json.get("message")
    channel_id = json.get("channel_id")
    if message and channel_id:
        handle_message(channel_id, message)


def stringify_transcript(channel_id, partial_message=None):
    messages = channel_transcript_map.get(channel_id)
    if messages is None:
        reset_transcript(channel_id)
        messages = channel_transcript_map.get(channel_id)
    transcript = ""
    for m in messages:
        if "role" in m:
            if m["role"] != "system":
                transcript += f'{m["content"]}'
        else:
            transcript += m
    if partial_message is not None:
        transcript += partial_message
    transcript = expand_slash_reply(transcript)
    # Include token usage and time information
    if channel_id in channel_cost_map:
        transcript += f'\n\nInput tokens: {channel_cost_map[channel_id]["input_tokens"]} Output tokens: {channel_cost_map[channel_id]["output_tokens"]} api_call_duration_sec: {channel_cost_map[channel_id]["time"]:.2f} model: {ANTHROPIC_MODEL}'
    return transcript


async def process_anthropic_stream(to_send, system_prompt):
    """Process a stream from Anthropic Claude API and return full results"""
    # Normalize messages format for Anthropic
    messages = []
    for msg in to_send:
        if msg["role"] == "system":
            # System prompts handled separately in Anthropic
            continue
        messages.append({"role": msg["role"], "content": msg["content"]})

    # Ensure the first message is from a user (Anthropic requirement)
    if messages and messages[0]["role"] != "user":
        messages = [{"role": "user", "content": "<car_enter>"}] + messages

    # Set up stream parameters
    stream_args = {
        "messages": messages,
        "model": ANTHROPIC_MODEL,
        "max_tokens": 8192,
    }

    # Add system prompt if available
    if system_prompt:
        # System prompt must be provided as text content
        stream_args["system"] = system_prompt

    # Create Anthropic client
    timeout = 10.0  # Adjust as needed
    api_key = os.getenv("ANTHROPIC_API_KEY")

    # If ANTHROPIC_API_KEY doesn't exist, try ANTHROPIC_SDK_KEY directly
    if not api_key:
        api_key = os.getenv("ANTHROPIC_SDK_KEY")
        if api_key:
            os.environ["ANTHROPIC_API_KEY"] = api_key
            print("Using ANTHROPIC_SDK_KEY for authentication")

    # Check if API key exists
    if not api_key:
        raise ValueError(
            "Neither ANTHROPIC_API_KEY nor ANTHROPIC_SDK_KEY environment variable is set"
        )

    anthropic_client = AsyncAnthropic(
        api_key=api_key,
        timeout=httpx.Timeout(timeout, read=timeout, write=timeout, connect=timeout),
    )

    collected_chunks = []
    request_start_time = time.time()
    first_token_time = None

    async with anthropic_client.messages.stream(**stream_args) as stream:
        async for chunk in stream.text_stream:
            if not first_token_time and chunk.strip():
                first_token_time = time.time()
            collected_chunks.append(chunk)
            yield {"type": "chunk", "text": chunk}

        # Get usage statistics
        final_message = await stream.get_final_message()
        usage = final_message.usage

        # Yield the final stats object as the last item in the stream
        yield {
            "type": "stats",
            "completion_tokens": usage.output_tokens,
            "prompt_tokens": usage.input_tokens,
            "total_time": time.time() - request_start_time,
            "time_to_first_token": (
                (first_token_time - request_start_time) if first_token_time else None
            ),
            "full_response": "".join(collected_chunks),
        }


def handle_message(channel_id, message):
    print("CHANNEL ID", channel_id)
    transcript = channel_transcript_map.get(channel_id)

    # Handle reset and debug commands
    if transcript is None or message.startswith("\\reset"):
        reset_transcript(channel_id)
        transcript = stringify_transcript(channel_id)
        emit(
            "my response", {"transcript": transcript}, broadcast=True
        )  # emit an event to the client
        return

    # Special debug command to check environment variables
    if message.startswith("\\debug"):
        debug_info = "Debug Information:\n"

        # Safely check API key (show prefix only)
        api_key = os.getenv("ANTHROPIC_API_KEY")
        sdk_key = os.getenv("ANTHROPIC_SDK_KEY")

        if api_key:
            prefix = api_key[:4] + "..." if len(api_key) > 4 else "***"
            debug_info += f"ANTHROPIC_API_KEY set: Yes (prefix: {prefix})\n"
        else:
            debug_info += "ANTHROPIC_API_KEY set: No\n"

        if sdk_key:
            prefix = sdk_key[:4] + "..." if len(sdk_key) > 4 else "***"
            debug_info += f"ANTHROPIC_SDK_KEY set: Yes (prefix: {prefix})\n"
        else:
            debug_info += "ANTHROPIC_SDK_KEY set: No\n"

        if not api_key and not sdk_key:
            # Try to reload credentials
            credentials_file = os.path.join(
                os.path.dirname(__file__), "credentials.toml"
            )
            debug_info += f"Attempting to reload credentials from {credentials_file}\n"
            if load_credentials_from_toml(credentials_file):
                debug_info += "Credentials loaded successfully\n"

                # Make ANTHROPIC_SDK_KEY available as ANTHROPIC_API_KEY
                if (
                    "ANTHROPIC_SDK_KEY" in os.environ
                    and "ANTHROPIC_API_KEY" not in os.environ
                ):
                    os.environ["ANTHROPIC_API_KEY"] = os.environ["ANTHROPIC_SDK_KEY"]
                    debug_info += "Set ANTHROPIC_API_KEY from ANTHROPIC_SDK_KEY\n"

                api_key = os.getenv("ANTHROPIC_API_KEY")
                sdk_key = os.getenv("ANTHROPIC_SDK_KEY")

                if api_key:
                    prefix = api_key[:4] + "..." if len(api_key) > 4 else "***"
                    debug_info += f"ANTHROPIC_API_KEY now set: Yes (prefix: {prefix})\n"

                if sdk_key:
                    prefix = sdk_key[:4] + "..." if len(sdk_key) > 4 else "***"
                    debug_info += f"ANTHROPIC_SDK_KEY now set: Yes (prefix: {prefix})\n"
            else:
                debug_info += "Failed to load credentials\n"

        debug_info += f"ANTHROPIC_MODEL: {ANTHROPIC_MODEL}\n"

        # List all loaded environment variables (excluding actual values)
        debug_info += "\nAll environment variables (excluding values):\n"
        for key in sorted(os.environ.keys()):
            if (
                "key" in key.lower()
                or "secret" in key.lower()
                or "token" in key.lower()
                or "password" in key.lower()
            ):
                debug_info += f"- {key}: ***\n"
            else:
                debug_info += f"- {key}: Set\n"

        # Add debug response to transcript
        transcript.append({"role": "assistant", "content": debug_info})
        channel_transcript_map[channel_id] = transcript
        emit(
            "my response",
            {"transcript": stringify_transcript(channel_id)},
            broadcast=True,
        )
        return

    message = asr_replace.replace(message)
    transcript.append({"role": "user", "content": f"\nCX: {message}\n"})

    to_send = deepcopy(transcript)

    # Extract system prompt and prepare messages
    system_prompt = None
    for i, msg in enumerate(to_send):
        if msg["role"] == "system":
            system_prompt = msg["content"]
            # Remove system message from to_send as it's handled separately in Anthropic
            to_send.pop(i)
            break

    # Simplify the last assistant message to avoid repetition
    last_assistant_index = None
    last_assistant_content = None
    for i, msg in enumerate(to_send):
        if msg["role"] == "assistant":
            last_assistant_index = i
            last_assistant_content = msg["content"]

    if last_assistant_index is not None:
        to_send[last_assistant_index]["content"] = last_assistant_content.split("\n")[0]

    # Set up asyncio for Anthropic's async client
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        collected_messages = []
        stream_generator = process_anthropic_stream(to_send, system_prompt)

        start_time = time.time()

        # Run the stream generator and capture results
        result = loop.run_until_complete(
            collect_stream_results(stream_generator, channel_id, collected_messages)
        )

        end_time = time.time()
        full_reply_content = result["full_response"]

        ai_selected_response = full_reply_content.split("\n")
        if ai_selected_response:
            ai_selected_response = ai_selected_response[0]
        else:
            ai_selected_response = full_reply_content
        print(f"AI Selected response: {ai_selected_response}")

        try:
            parsed_cart = parse_cart(full_reply_content.split("\n")[1:])
            print("Parsed Cart:")
            print_prp_cart(parsed_cart)
        except Exception:
            print("FAILED TO PARSE CART")
            traceback.print_exc()

        transcript.append({"role": "assistant", "content": full_reply_content})

        # Update token usage and timing information
        channel_cost_map[channel_id] = {
            "input_tokens": result.get("prompt_tokens", 0),
            "output_tokens": result.get("completion_tokens", 0),
            "time": end_time - start_time,
        }

    except Exception as e:
        print(f"Error processing message: {str(e)}")
        traceback.print_exc()
        transcript.append({"role": "assistant", "content": f"Error: {str(e)}"})

    channel_transcript_map[channel_id] = transcript
    return stringify_transcript(channel_id)


async def collect_stream_results(stream_generator, channel_id, collected_messages):
    """Helper function to collect streaming results from Anthropic API"""
    result = None
    async for item in stream_generator:
        if item["type"] == "stats":
            # This is the final stats object
            result = item
        elif item["type"] == "chunk":
            # This is a text chunk
            collected_messages.append(item["text"])
            emit(
                "my response",
                {
                    "transcript": stringify_transcript(
                        channel_id, "".join(collected_messages)
                    )
                },
                broadcast=True,
            )

    if not result:
        # If we didn't get a result object, create one with the collected text
        result = {
            "full_response": "".join(collected_messages),
            "prompt_tokens": 0,
            "completion_tokens": 0,
        }

    return result


# pylint: disable=unused-argument
def lambda_handler(event, context):
    from werkzeug.wrappers import Request

    request.environ["x-amz-invocation-type"] = (
        "RequestResponse"  # Set a special header to indicate that we're running on AWS Lambda
    )
    flask_request = Request(request.environ)
    with app.request_context(flask_request.environ):
        return app.full_dispatch_request()


if args.local:
    socketio.run(app, port=3000, debug=True)
else:
    socketio.run(app, host="0.0.0.0", port=3000, allow_unsafe_werkzeug=True, debug=True)
