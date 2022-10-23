"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note:
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.


Tests:
- Test 1
    - Input: 07:05:45PM
    - Out: 19:05:45
- Test 2
    - Input: 12:45:54PM
    - Out: 12:45:54
- Test 3
    - Input: 12:40:22AM
    - Out: 00:40:22
- Test 4
    - Input: 07:05:45AM
    - Out: 07:05:45
"""


def convert_time(input_time):
    hour = int(input_time[0:2])
    minute_second = input_time[3:8]
    hour_format = input_time[8:10]

    if hour_format == "PM" and hour != 12:
        hour += 12

    if hour_format == "AM" and hour == 12:
        hour = "00"

    return f"{hour}:{minute_second}"


print(convert_time("07:05:45PM"))
print(convert_time("12:45:54PM"))
print(convert_time("12:40:22AM"))
print(convert_time("07:05:45AM"))
print(convert_time("12:00:00AM"))
print(convert_time("12:00:00PM"))



