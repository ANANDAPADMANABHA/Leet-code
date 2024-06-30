class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pl , pr = 0, len(numbers)-1
        ans = []
        while pl<pr:
                
            if  numbers[pl]+numbers[pr] > target:
                pr -=1
                
            elif numbers[pl]+numbers[pr] < target:
                pl +=1
                
            else:
                return [pl+1,pr+1]
                
            