class Solution:
    def fib(self, n):
        if n <= 1:
            return n

        a, b = 0, 1

        for i in range(2,  n + 1):
            a, b = b, a + b

        return b


s = Solution()
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))
