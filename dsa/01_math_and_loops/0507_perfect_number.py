"""
507. Perfect Number
https://leetcode.com/problems/perfect-number/
Difficulty: Easy | Topic: Math & Loops

Approach: divisors come in pairs (for 28: 1 x 28, 2 x 14, 4 x 7), so only loop while
i * i <= num. Each time i divides num, add both i and num // i.
Start with total = 1 and i = 2, because 1 always counts but its pair (num itself) must not.

Time:  O(sqrt(n)), about 10,000 steps for num = 10^8
Space: O(1)

First attempt: loop from 1 to num // 2 and add every divisor. The logic was correct,
but it's O(n): 50 million steps for num = 10^8, which gets TLE in Python.

Lessons:
- O(n / 2) is still O(n). Big-O ignores constant factors, so halving a loop isn't enough;
  you have to change how the work grows
- Divisor pairs: only check up to sqrt(n). `i * i <= num` avoids computing a square root
- Perfect squares: for 16, the pair 4 x 4 must only be added once (`if i != num // i`)
- Don't name a variable `sum`, and remove debug prints (they're slow inside big loops)
- `return total == num` instead of a temp `ans` variable
"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        total = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
            i += 1

        return total == num


if __name__ == "__main__":
    s = Solution()
    assert s.checkPerfectNumber(28) is True
    assert s.checkPerfectNumber(7) is False
    assert s.checkPerfectNumber(6) is True
    assert s.checkPerfectNumber(1) is False
    assert s.checkPerfectNumber(16) is False
    assert s.checkPerfectNumber(33550336) is True
    print("All tests passed ✅")
