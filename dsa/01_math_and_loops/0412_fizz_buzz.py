"""
412. Fizz Buzz
https://leetcode.com/problems/fizz-buzz/
Difficulty: Easy | Topic: Math & Loops

Approach: loop from 1 to n. Check the FizzBuzz case (divisible by 3 AND 5) first,
because the first true branch of an if/elif chain wins.

Time:  O(n), one pass from 1 to n
Space: O(n), the output list holds n strings

Lessons:
- In Python you create a list with `ans = []`, not `ans[n] = []` (no fixed size)
- Use `.append(x)` to add to a list. `ans[i] = x` only works if position i already exists
- `( )` calls a method, `[ ]` indexes. `"i"` is the letter i, `str(i)` is the number as text
- `range(1, n + 1)` gives 1..n (the stop value is never included)
"""


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:
                ans.append("FizzBuzz")
            elif i % 5 == 0:
                ans.append("Buzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            else:
                ans.append(str(i))

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.fizzBuzz(3) == ["1", "2", "Fizz"]
    assert s.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert s.fizzBuzz(15)[-1] == "FizzBuzz"
    print("All tests passed ✅")
