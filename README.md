# DSA in Python 🐍

My journey learning **Data Structures & Algorithms in Python**, from the basics up, with practice on [LeetCode](https://leetcode.com/).

**Goal:** solve LeetCode easy/medium problems on my own and explain their time and space complexity, the level needed for an **AI / Agentic AI Developer** role.

## Progress

| Solved | Easy | Medium | Hard |
|---|---|---|---|
| **8** | 8 | 0 | 0 |

The full roadmap (about 200 problems, grouped by topic) is in [LEETCODE.md](LEETCODE.md).

## Solved problems

### 01 · Math & Loops
| # | Problem | Difficulty | Key idea | Time | Space | Solution |
|---|---|---|---|---|---|---|
| 412 | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Easy | if/elif order matters | O(n) | O(n) | [code](dsa/01_math_and_loops/0412_fizz_buzz.py) |
| 1342 | [Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) | Easy | halving loop | O(log n) | O(1) | [code](dsa/01_math_and_loops/1342_number_of_steps_to_reduce_a_number_to_zero.py) |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | digit-peeling + rebuild | O(log n) | O(1) | [code](dsa/01_math_and_loops/0009_palindrome_number.py) |
| 1281 | [Subtract the Product and Sum of Digits](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/) | Easy | digit-peeling | O(log n) | O(1) | [code](dsa/01_math_and_loops/1281_subtract_the_product_and_sum_of_digits.py) |
| 2520 | [Count the Digits That Divide a Number](https://leetcode.com/problems/count-the-digits-that-divide-a-number/) | Easy | digit-peeling on a copy | O(log n) | O(1) | [code](dsa/01_math_and_loops/2520_count_the_digits_that_divide_a_number.py) |
| 258 | [Add Digits](https://leetcode.com/problems/add-digits/) | Easy | nested loop / digital root | O(log n) | O(1) | [code](dsa/01_math_and_loops/0258_add_digits.py) |
| 1523 | [Count Odd Numbers in an Interval Range](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/) | Easy | math formula, no loop | O(1) | O(1) | [code](dsa/01_math_and_loops/1523_count_odd_numbers_in_an_interval_range.py) |
| 2427 | [Number of Common Factors](https://leetcode.com/problems/number-of-common-factors/) | Easy | loop to min(a, b) | O(min(a, b)) | O(1) | [code](dsa/01_math_and_loops/2427_number_of_common_factors.py) |

## Repo layout

```
dsa/
  01_math_and_loops/
    0412_fizz_buzz.py      # one file per problem: notes + solution + tests
  02_arrays/               # (coming next)
  ...
LEETCODE.md                # full roadmap with checkboxes
```

Each solution file has:
- the problem link, difficulty and topic
- the approach, plus time and space complexity
- **lessons**: the mistakes I made and what I learned
- tests using LeetCode's examples

## Running a solution

This project uses [uv](https://docs.astral.sh/uv/).

```bash
uv run dsa/01_math_and_loops/0412_fizz_buzz.py
```

It prints `All tests passed ✅` if the solution is correct.
