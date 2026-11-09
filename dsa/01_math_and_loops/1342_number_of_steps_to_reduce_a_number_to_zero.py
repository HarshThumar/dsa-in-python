"""
1342. Number of Steps to Reduce a Number to Zero
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
Difficulty: Easy | Topic: Math & Loops

Approach: while num > 0, halve it if it's even, otherwise subtract 1. Count the steps.

Time:  O(log n), every even step halves the number
Space: O(1), just one counter

Lessons:
- Python doesn't need `;` at the end of lines
- Give counters clear names (`steps`, not `n`)
- If both branches of an if/else do the same thing (`n += 1`), move it out of the if/else
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
                n += 1
            else:
                num -= 1
                n += 1

        return n


if __name__ == "__main__":
    s = Solution()
    assert s.numberOfSteps(14) == 6
    assert s.numberOfSteps(8) == 4
    assert s.numberOfSteps(123) == 12
    print("All tests passed ✅")
