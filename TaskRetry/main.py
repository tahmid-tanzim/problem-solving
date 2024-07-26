import asyncio
from tenacity import retry, stop_after_attempt, before_log, retry_if_result, RetryError, after_log
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

logger = logging.getLogger(__name__)

FINDING_AGENT_RETRY_ATTEMPT = 2


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
    'attempt_index': 0,
    'key': 'test_3'
}


def log_attempt_number(retry_state):
    """return the result of the last call attempt"""
    logger.error(f"Retry Done: {retry_state.attempt_number}...")


def is_none_retry_value(value) -> bool:
    return value is None


async def find_available_agents(session_id):
    print('Start find_available_agents', test_suite['key'], test_suite['attempt_index'])
    await asyncio.sleep(2)
    output = test_suite[test_suite['key']][test_suite['attempt_index']]
    print('End find_available_agents', session_id)
    test_suite['attempt_index'] += 1
    return output


@retry(stop=stop_after_attempt(FINDING_AGENT_RETRY_ATTEMPT),
       retry=retry_if_result(is_none_retry_value),
       before=before_log(logger, logging.INFO),
       after=after_log(logger, logging.INFO))
async def stop_after_n_attempts(session_id):
    return await find_available_agents(session_id)


async def main():
    try:
        session_id = 123
        agents = await stop_after_n_attempts(session_id)
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

    asyncio.run(main())


