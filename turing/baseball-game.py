#!/usr/bin/python3
# https://leetcode.com/problems/baseball-game/

def cal_points(ops):
    score = 0
    previous = []

    for val in ops:
        if val == "+":
            sum_of_prev_2_number = previous[-2] + previous[-1]
            score += sum_of_prev_2_number
            previous.append(sum_of_prev_2_number)
        elif val == "D":
            double_last_number = 2 * previous[-1]
            score += double_last_number
            previous.append(double_last_number)
        elif val == "C":
            last_number = previous.pop()
            score -= last_number
        else:
            number = int(val)
            score += number
            previous.append(number)

    return score


if __name__ == "__main__":
    """
    1. "integer" - add new score
    2. "+"       - sum of previous 2 score
    3. "D"       - double previous score
    4. "C"       - remove previous score
    """
    print(cal_points(["5", "2", "C", "D", "+"]))  # 30
    print(cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # 27

