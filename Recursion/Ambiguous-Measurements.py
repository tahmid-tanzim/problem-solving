#!/usr/bin/python3
# https://www.algoexpert.io/questions/Ambiguous%20Measurements
"""
  This problem deals with measuring cups that are missing important measuring
  labels. Specifically, a measuring cup only has two measuring lines, a Low (L)
  line and a High (H) line. This means that these cups can't precisely measure
  and can only guarantee that the substance poured into them will be between the
  L and H line. For example, you might have a measuring cup that has a Low line
  at 400ml and a high line at 435ml. This means that
  when you use this measuring cup, you can only be sure that what you're
  measuring is between 400ml and 435ml.

  You're given a list of measuring cups containing their low and high lines as
  well as one low integer and one high integer
  representing a range for a target measurement. Write a function that returns a
  boolean representing whether you can use the cups to accurately measure a
  volume in the specified [low, high] range (the range is
  inclusive).

Note that:

    1. Each measuring cup will be represented by a pair of positive integers
    [L, H], where 0 &lt;= L &lt;= H.

    2. You'll always be given at least one measuring cup, and the
    low and high input parameters will always satisfy
    the following constraint: 0 &lt;= low &lt;= high.

    3. Once you've measured some liquid, it will immediately be transferred to a
    larger bowl that will eventually (possibly) contain the target measurement.
  
    4. You can't pour the contents of one measuring cup into another cup.

Sample Input
measuringCups = [
  [200, 210],
  [450, 465],
  [800, 850],
] 
low = 2100
high = 2300

Sample Output
true
// We use cup [450, 465] to measure four volumes:
// First measurement: Low = 450, High = 465
// Second measurement: Low = 450 + 450 = 900, High = 465 + 465 = 930
// Third measurement: Low = 900 + 450 = 1350, High = 930 + 465 = 1395
// Fourth measurement: Low = 1350 + 450 = 1800, High = 1395 + 465 = 1860

// Then we use cup [200, 210] to measure two volumes:
// Fifth measurement: Low = 1800 + 200 = 2000, High = 1860 + 210 = 2070
// Sixth measurement: Low = 2000 + 200 = 2200, High = 2070 + 210 = 2280

// We've measured a volume in the range [2200, 2280].
// This is within our target range, so we return `true`.

// Note: there are other ways to measure a volume in the target range.
"""


# O(low * high * n) time | O(low * high) space
# where n is the number of measuring cups
class Solution1:
    def measurementsHelper(self, measuringCups, low, high, L, H, memoize):
        # Base Case
        if (H > high and low <= L <= high) or (high < L <= H):
            return False

        key = f'{L}-{H}'
        if key in memoize:
            return memoize[key]

        isValidMeasurement = False
        for [smallCup, largeCup] in measuringCups:
            if low <= L + smallCup and H + largeCup <= high:
                isValidMeasurement = True
                break
            isValidMeasurement = self.measurementsHelper(measuringCups, low, high, L + smallCup, H + largeCup, memoize)
            if isValidMeasurement:
                break
        memoize[key] = isValidMeasurement
        return isValidMeasurement

    def ambiguousMeasurements(self, measuringCups, low, high):
        return self.measurementsHelper(measuringCups, low, high, 0, 0, {})


class Solution2:
    def measurementsHelper(self, measuringCups, low, high, L, H, memoize):
        # Base Case
        if low <= L and H <= high:
            return True
        if (H > high and low <= L <= high) or (high < L <= H):
            return False

        # Return Cache Value
        key = f'{L}-{H}'
        if key in memoize:
            return memoize[key]

        isValidMeasurement = False
        for [smallCup, largeCup] in measuringCups:
            isValidMeasurement = isValidMeasurement or self.measurementsHelper(measuringCups, low, high, L + smallCup,
                                                                               H + largeCup, memoize)
        memoize[key] = isValidMeasurement
        return isValidMeasurement

    def ambiguousMeasurements(self, measuringCups, low, high):
        return self.measurementsHelper(measuringCups, low, high, 0, 0, {})


if __name__ == "__main__":
    s1 = Solution1()
    print(f'Output - {s1.ambiguousMeasurements([[200, 210], [450, 465], [800, 850]], 2100, 2300)}')
    s2 = Solution2()
    print(f'Output - {s2.ambiguousMeasurements([[200, 210], [450, 465], [800, 850]], 2100, 2300)}')
