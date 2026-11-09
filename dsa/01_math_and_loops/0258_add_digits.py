"""
258. Add Digits
https://leetcode.com/problems/add-digits/
Difficulty: Easy | Topic: Math & Loops

Approach: a nested loop. The inner loop adds up the digits once (digit-peeling).
The outer loop repeats that until only one digit is left. The key line is
`num = total`, which feeds the result back into the outer loop.

Time:  O(log n), the first round is one pass per digit, and later rounds are tiny
Space: O(1)

Follow-up, O(1) (digital root): adding digits doesn't change the remainder mod 9,
because 10, 100, 1000... are each 1 more than a multiple of 9.
So the answer is num % 9, except it's 9 when that's 0 (and 0 when num is 0).
TODO: write the O(1) version yourself.

Lessons:
- Pattern: "repeat X until a condition holds" = an outer while loop around the code that does X once
- In an interview, give the loop solution first, then mention the math trick
"""


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num = num // 10
            num = total
        return num


if __name__ == "__main__":
    s = Solution()
    assert s.addDigits(38) == 2
    assert s.addDigits(0) == 0
    assert s.addDigits(9875) == 2
    print("All tests passed ✅")
