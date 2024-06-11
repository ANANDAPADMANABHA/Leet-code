class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = 0
        k = 0
        for i in nums:
            if i != val:
                nums[p] = i
                k +=1
                p +=1
        return k