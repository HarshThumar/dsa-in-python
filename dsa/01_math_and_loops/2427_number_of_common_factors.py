"""
2427. Number of Common Factors
https://leetcode.com/problems/number-of-common-factors/
Difficulty: Easy | Topic: Math & Loops

Approach: a common factor can't be bigger than the smaller number, so loop from 1 to
min(a, b) and count the numbers that divide both.

Time:  O(min(a, b)), the loop runs once per number up to the smaller input
Space: O(1)

Lessons:
- Use the built-in `min(a, b)` instead of an if/else to pick the smaller value
- Bonus: every common factor divides gcd(a, b) (`math.gcd`), so you could count the
  divisors of the gcd instead, using the "divisors come in pairs" trick
"""


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        low = 0
        ans = 0
        if a > b:
            low = b
        else:
            low = a

        for i in range(1, low + 1):
            if a % i == 0 and b % i == 0:
                ans += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.commonFactors(12, 6) == 4
    assert s.commonFactors(25, 30) == 2
    print("All tests passed ✅")
