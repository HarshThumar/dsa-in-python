"""
1281. Subtract the Product and Sum of Digits of an Integer
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
Difficulty: Easy | Topic: Math & Loops

Approach: digit-peeling. Keep a running sum (starts at 0) and product (starts at 1, not 0!).

Time:  O(log n), one loop per digit
Space: O(1)

Lessons:
- Operator precedence: `*` and `%` have the same priority and run left to right.
  `product * n % 10` means `(product * n) % 10`. Add brackets: `product * (n % 10)`
- Don't name a variable `sum`, because that hides the built-in sum() function
- Remove debug prints before submitting
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum2 = 0
        product = 1
        while n > 0:
            sum2 = sum2 + n % 10
            product = product * (n % 10)
            n = n // 10

        return product - sum2


if __name__ == "__main__":
    s = Solution()
    assert s.subtractProductAndSum(234) == 15
    assert s.subtractProductAndSum(4421) == 21
    print("All tests passed ✅")
