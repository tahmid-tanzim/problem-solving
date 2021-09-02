#!/usr/bin/python3

def smallestDifference(arrayOne, arrayTwo):
    minDiff = float("inf")
    output = []
    i = 0
    j = 0

    arrayOne.sort()
    arrayTwo.sort()

    while i < len(arrayOne) and j < len(arrayTwo):
        first_val = arrayOne[i]
        second_val = arrayTwo[j]

        if first_val < second_val:
            currentDiff = abs(second_val - first_val)
            i += 1
        elif second_val < first_val:
            currentDiff = abs(first_val - second_val)
            j += 1
        else:
            return [first_val, second_val]

        if currentDiff < minDiff:
            minDiff = currentDiff
            output = [first_val, second_val]

    return output


if __name__ == "__main__":
    print(smallestDifference([- 1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
