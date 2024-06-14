class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prviousmap = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in prviousmap:
                return [i,prviousmap[dif]]
            prviousmap[nums[i]] = i