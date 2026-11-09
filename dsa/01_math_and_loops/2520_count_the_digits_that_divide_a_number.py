"""
2520. Count the Digits That Divide a Number
https://leetcode.com/problems/count-the-digits-that-divide-a-number/
Difficulty: Easy | Topic: Math & Loops

Approach: save a copy of the original number, then peel digits off the other one
and check whether each digit divides the original.

Time:  O(log n), one loop per digit
Space: O(1)

Lessons:
- `num // 10` on its own line computes a value and throws it away. To change num,
  assign it back: `num = num // 10`. Forgetting this = infinite loop
- Time Limit Exceeded on a tiny input (like 7) almost always means an infinite loop
- Read the constraints: "num does not contain 0 as a digit" is why `temp % 0` can't happen
"""


class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        temp = num
        while num > 0:
            if temp % (num % 10) == 0:
                ans += 1

            num = num // 10
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.countDigits(7) == 1
    assert s.countDigits(121) == 2
    assert s.countDigits(1248) == 4
    print("All tests passed ✅")
