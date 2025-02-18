'''
202. Happy Number
Link: https://leetcode.com/problems/happy-number/
Resource: https://bit.ly/3MGcBog

Write an algorithm to determine if a number n is 'happy'.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Examples:
1. 19 -> true
Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}

        while n:
            n = self.squared(n)

            if n == 1:
                return True
            if n in seen:
                return False

            seen.add(n)

    def is_happy_v2(self, n: int) -> bool:
        slow = self.squared(n)
        fast = self.squared(slow)

        while slow != fast:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))

        return slow == 1

    def squared(self, n: int) -> int:
        squares = [int(x) ** 2 for x in str(n)]
        return sum(squares)

    def squared_v2(self, n: int) -> int:
        result = 0

        while n > 0:
            n, last = divmod(n, 10)
            result += last * last

        return result


soln = Solution()
assert soln.is_happy(19) == True
