class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n & n-1  == 0 and n > 0:
            return True
        return False