class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return x
            if n == 1:
                return x
            if n % 2 == 0:
                half = helper(x, n // 2)
                return half * half
            else:
                return x * helper(x, n - 1)
        if n == 0:
            return 1
        elif n > 0:
            return helper(x, n)
        else:
            val = helper(x, -n)
            return 1 / val
