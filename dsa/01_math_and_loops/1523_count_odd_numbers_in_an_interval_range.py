"""
1523. Count Odd Numbers in an Interval Range
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
Difficulty: Easy | Topic: Math & Loops

Approach: count the odd numbers in 1..high, subtract the odd numbers in 1..low,
then add 1 back if low itself is odd (because subtracting removed it).

Time:  O(1), no loops, just arithmetic
Space: O(1)

The first try was a loop from low to high, which is O(n) and got Time Limit Exceeded,
since high - low can be ~10^9 and Python does roughly 10^7 simple steps per second.
Read the constraints first!

Shorter version of the same idea:
    odds in 1..x       = (x + 1) // 2
    odds in 1..low - 1 = low // 2
    answer             = (high + 1) // 2 - low // 2

Lessons:
- Test a formula against a table of small cases (caught x // 2 + 1 being wrong for even x)
- `i += 1` inside a `for` loop does nothing. The for loop sets i again each round
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low_odd = 0
        high_odd = 0
        if low % 2 == 0:
            low_odd = low // 2
        else:
            low_odd = (low // 2) + 1

        if high % 2 == 0:
            high_odd = high // 2
        else:
            high_odd = (high // 2) + 1

        if low % 2 == 0:
            return high_odd - low_odd
        else:
            return high_odd - low_odd + 1


if __name__ == "__main__":
    s = Solution()
    assert s.countOdds(3, 7) == 3
    assert s.countOdds(8, 10) == 1
    assert s.countOdds(0, 0) == 0
    assert s.countOdds(798273637, 970699661) == (970699661 + 1) // 2 - 798273637 // 2
    print("All tests passed ✅")
