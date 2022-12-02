#!/usr/bin/python3
from typing import List


def optimal_routes(times: List[int], max_hour_limit: int, index: int, combination: List[int]) -> List[List[int]]:
    if max_hour_limit == 0:
        return [combination]
    if max_hour_limit < 0:
        return list()

    results = list()
    for next_index in range(index, len(times)):
        if next_index > index and times[next_index] == times[next_index - 1]:
            continue
        if max_hour_limit - times[next_index] < 0:
            break

        temp = combination.copy()
        temp.append(times[next_index])
        results += optimal_routes(times, max_hour_limit - times[next_index], next_index + 1, temp)
    return results


if __name__ == '__main__':
    print('-------------------------------------')
    hour_group = (24, 28, 33.5, 42, 56, 84, 168)
    for hour in hour_group:
        combinations = optimal_routes([5.5, 6.25, 6.75, 7, 7, 7.5, 9.25, 12, 12.5, 14], hour, 0, [])
        print(f'For {hour}hr ', end='combinations are: \n' if len(combinations) > 0 else 'NO combinations found!!\n')
        for item in combinations:
            print('\t', item)
        print('-------------------------------------')
