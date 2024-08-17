import asyncio
from tenacity import retry, before_sleep_log, wait_random_exponential, wait_fixed, stop_after_delay, wait_random_exponential, before_sleep_log, stop_after_attempt, before_log, retry_if_result, RetryError, after_log
import logging
import sys
import datetime

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

logger = logging.getLogger(__name__)

FINDING_AGENT_RETRY_ATTEMPT = 2
AGENT_RETRY_MAX_WAIT = 10
AGENT_RETRY_MAX_WAIT_2 = 2
AGENT_SEARCH_WAIT_ATTEMPT = 10
AGENT_RETRY_STOP_AFTER_DELAY = 30


def build_authorized_agents_default() -> dict:
    return {"id_and_time_map": [], "agents_details": {}}


authorized_agents = {
    "id_and_time_map": [],
    "agents_details": {
        3910: {
            "name": "Tahmid Tanzim",
            "email": "tahmid.tanzim@gmail.com"
        },
        3543: {
            "name": "Kazi Fatiha Akram",
            "email": "kazi.fatiha.akram@gmail.com"
        },
        3703: {
            "name": "Serhan Kazi Tanzim",
            "email": "serhan.kazi.tanzim@gmail.com"
        }
    }
}


test_suite = {
    'test_1': [authorized_agents, 'Invalid State 1', 'Invalid State 2', 'Invalid State 3'],
    'test_2': [None, authorized_agents, 'Invalid State 2', 'Invalid State 3'],
    'test_3': [None, None, 'Invalid State 2', 'Invalid State 3'],  # default
    'test_4': [None, None, authorized_agents, 'Invalid State 3'],  # default
    'test_5': [None, None, None, None, None, None, None, None, None, None, None, None, authorized_agents, None, None, None, None],  # default
    'attempt_index': 0,
    'key': 'test_5'
}


def log_attempt_number(retry_state):
    """return the result of the last call attempt"""
    logger.error(f"Retry Done: {retry_state.attempt_number}...")


def is_none_retry_value(value) -> bool:
    return value is None


async def find_available_agents(session_id):
    print('Start find_available_agents', test_suite['key'], test_suite['attempt_index'])
    await asyncio.sleep(1)
    output = test_suite[test_suite['key']][test_suite['attempt_index']]
    print('End find_available_agents', session_id)
    test_suite['attempt_index'] += 1
    return output


@retry(reraise=True,
       before_sleep=before_sleep_log(logger, logging.INFO),
       after=after_log(logger, logging.INFO),
       wait=wait_fixed(AGENT_RETRY_MAX_WAIT_2),
       retry=retry_if_result(is_none_retry_value),
       stop=stop_after_delay(AGENT_RETRY_STOP_AFTER_DELAY))
async def stop_after_30_sec(session_id, attempt):
    logger.info(f"\n\nRetrying: {session_id}...{attempt['number']}")
    attempt["number"] += 1
    return await find_available_agents(session_id)


async def main():
    try:
        session_id = 123
        attempt = {"number": 1}
        # agents = await stop_after_n_attempts(session_id, attempt)
        agents = await stop_after_30_sec(session_id, attempt)
        print('Available agents: ', agents)
    except RetryError as e:
        logger.error(f"Error: handle_authorized_agents {e}")
        print(build_authorized_agents_default())


if __name__ == "__main__":
    # test_suite['attempt_index'] = 0
    # test_suite['key'] = 'test_1'
    # asyncio.run(main())

    # test_suite['attempt_index'] = 0
    # test_suite['key'] = 'test_2'
    # asyncio.run(main())
    # test_suite['attempt_index'] += 1
    # asyncio.run(main())

    # test_suite['attempt_index'] = 0
    # test_suite['key'] = 'test_3'
    # asyncio.run(main())
    # test_suite['attempt_index'] += 1
    # asyncio.run(main())
    # test_suite['attempt_index'] += 1
    # asyncio.run(main())

    AGENT_SEARCH_ATTEMPT = 2
    session_id = '3123123adasd'
    # print(f"Error: No authorized agent found after {AGENT_SEARCH_ATTEMPT} more retries",
    # f"for session_id: {session_id}.")

    asyncio.run(main())



