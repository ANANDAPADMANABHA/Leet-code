class Solution:
    def fib(self, n: int) -> int:
        def fibonacci(n):
            
            if n== 0 or n==1:
                return n
            return fibonacci(n-1)+fibonacci(n-2)
        
        return fibonacci(n)