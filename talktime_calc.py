#!/usr/local/bin/python3


def get_slot(time, is_start_time=True):
    if 0 <= time < 360:
        return 1, 360 - time if is_start_time else time
    elif 360 <= time < 720:
        return 2, 720 - time if is_start_time else time - 360
    elif 720 <= time < 1080:
        return 3, 1080 - time if is_start_time else time - 720
    else:
        return 4, 1440 - time if is_start_time else time - 1080


def get_talk_time(start, end):
    call_charge = 0
    start_date_str, start_time_str = start.split(' ')
    end_date_str, end_time_str = end.split(' ')

    s_year, s_month, s_day = tuple(map(int, start_date_str.split('-')))
    s_hour, s_minute, s_second = tuple(map(int, start_time_str.split(':')))
    e_year, e_month, e_day = tuple(map(int, end_date_str.split('-')))
    e_hour, e_minute, e_second = tuple(map(int, end_time_str.split(':')))

    # print(s_year, s_month, s_day)
    # print(e_year, e_month, e_day)
    # print(s_hour, s_minute, s_second)
    # print(e_hour, e_minute, e_second)
    delta_date = e_day - s_day + 1

    # Calculate Call Charge in Middle Days
    if delta_date > 2:
        # Avg Rate = Tk 2.5/Minute
        call_charge += (delta_date - 2) * 24 * 60 * 2.5
        print('Calculate Call Charge in Middle Days - ', call_charge)

    # Calculate Call Charge in Time
    # Check IF Remaining FULL DAY
    if s_hour == e_hour and s_minute == e_minute:
        call_charge += 24 * 60 * 2.5
        print('Check IF FULL DAY - ', call_charge)
    else:
        start_time = s_hour * 60 + s_minute
        end_time = e_hour * 60 + e_minute

        delta_time = abs(start_time - end_time)
        (start_rate, start_fraction_time) = get_slot(start_time, True)
        (end_rate, end_fraction_time) = get_slot(end_time, False)

        print('Start - ', start_rate, start_fraction_time)
        print('End - ', end_rate, end_fraction_time)

        if start_rate == end_rate:
            if start_time > end_time:
                # e.g. start time  8:00 | end time 7:00
                call_charge += (24 * 60 * 2.5) - (delta_time * start_rate)
                print('same slot (start_time > end_time) - ', call_charge)
            else:
                # e.g. start time  7:00 | end time 8:00
                call_charge += delta_time * start_rate
                print('same slot (start_time <= end_time) - ', call_charge)
        else:
            if start_rate > end_rate:
                # START -> 00:00
                i = start_rate
                while i <= 4:
                    if i == start_rate:
                        call_charge += start_fraction_time * start_rate
                    else:
                        call_charge += 360 * i
                    i += 1

                # 00:00 -> END
                i = 1
                while i <= end_rate:
                    if i == end_rate:
                        call_charge += end_fraction_time * end_rate
                    else:
                        call_charge += 360 * i
                    i += 1
            else:
                # START -> END
                i = start_rate
                while i <= end_rate:
                    if i == start_rate:
                        call_charge += start_fraction_time * start_rate
                    elif i == end_rate:
                        call_charge += end_fraction_time * end_rate
                    else:
                        call_charge += 360 * i
                    i += 1

    return call_charge


if __name__ == "__main__":
    start_datetime = '2020-10-01 07:00:00'
    end_datetime = '2020-10-02 08:00:00'
    print(f'BDT {get_talk_time(start_datetime, end_datetime)}')
