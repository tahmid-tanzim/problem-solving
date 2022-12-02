#!/usr/bin/python3


def weekly_schedule(flights):
    if len(flights) < 6:
        return list()

    flights = sorted(flights, key=lambda d: d["duration"], reverse=True)

    if flights[0]["duration"] > 48:
        return list()

    schedule = []
    while len(flights) > 0:
        i = 0
        n = len(flights)
        

    return schedule


if __name__ == "__main__":
    test_cases = [
        # {
        #     "input": (
        #         {"code": "SEA", "duration": 30.75},
        #         {"code": "YVR", "duration": 30.25},
        #         {"code": "IAD", "duration": 31.75},
        #         {"code": "CHC", "duration": 30.25},
        #         {"code": "PHL", "duration": 31.25},
        #         {"code": "SHA", "duration": 13.75},
        #     ),
        #     "output": True
        # },
        {
            "input": (
                {"code": "DDD", "duration": 20},
                {"code": "BBB", "duration": 42},
                {"code": "EEE", "duration": 18},
                {"code": "AAA", "duration": 44},
                {"code": "FFF", "duration": 10},
                {"code": "CCC", "duration": 34},
            ),
            "output": True
        },
        # {
        #     "input": (
        #         {"code": "AAA", "duration": 12},
        #         {"code": "BBB", "duration": 12},
        #         {"code": "CCC", "duration": 12},
        #         {"code": "DDD", "duration": 12},
        #         {"code": "EEE", "duration": 12},
        #         {"code": "FFF", "duration": 12},
        #         {"code": "GGG", "duration": 12},
        #         {"code": "HHH", "duration": 12},
        #         {"code": "III", "duration": 12},
        #         {"code": "JJJ", "duration": 12},
        #         {"code": "KKK", "duration": 12},
        #         {"code": "LLL", "duration": 12},
        #         {"code": "MMM", "duration": 12},
        #         {"code": "NNN", "duration": 12},
        #     ),
        #     "output": True
        # },
        # {
        #     "input": (
        #         {"code": "DDD", "duration": 27},
        #         {"code": "BBB", "duration": 42},
        #         {"code": "EEE", "duration": 26},
        #         {"code": "AAA", "duration": 44},
        #         {"code": "CCC", "duration": 29},
        #     ),
        #     "output": False
        # },
        # {
        #     "input": (
        #         {"code": "DDD", "duration": 17},
        #         {"code": "BBB", "duration": 39},
        #         {"code": "EEE", "duration": 18},
        #         {"code": "AAA", "duration": 49},
        #         {"code": "FFF", "duration": 16},
        #         {"code": "CCC", "duration": 29},
        #     ),
        #     "output": False
        # },
    ]

    for idx, test_case in enumerate(test_cases):
        schedule = weekly_schedule(test_case["input"])
        if len(schedule) > 0:
            print(schedule)
        else:
            print("Weekly Schedule is not possible")


