"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/
Difficulty: Easy | Topic: Math & Loops

Approach: reverse the number with digit-peeling (`x % 10` takes the last digit,
`x // 10` removes it) and build the reversed number (`ans * 10 + digit`).
Then compare it with the original. Negative numbers never enter the loop,
so ans stays 0 and they correctly return False.

Time:  O(log n), one loop per digit (a number n has about log10(n) digits)
Space: O(1)

Lessons:
- If a function ends without reaching a `return`, it returns None (LeetCode shows `null`).
  Every path through the function needs a return.
- `ans == check` is already True/False, so `return ans == check` replaces the if + temp variable
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = 0
        check = x
        temp = False

        while x > 0:
            ans = ans * 10 + x % 10
            x = x // 10

        if ans == check:
            temp = True
        return temp


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(121) is True
    assert s.isPalindrome(-121) is False
    assert s.isPalindrome(10) is False
    assert s.isPalindrome(0) is True
    print("All tests passed ✅")
