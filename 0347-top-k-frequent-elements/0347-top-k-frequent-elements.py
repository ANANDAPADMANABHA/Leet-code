class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}
        for i in nums:
            counter[i] = counter.get(i,0)+1
            
        nums_list = [[] for _ in range(len(nums)+1)]
        
        for num,count in counter.items():
            nums_list[count].append(num)
            
        ans = []
        
        for i in range(len(nums),0,-1):
            for j in nums_list[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans
            
                