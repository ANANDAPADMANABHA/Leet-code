class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = {
            "ans1": 0,
            "ans2": 0
        }
        
        for i in nums1:
                if i in nums2 :
                    ans["ans1"] += 1
                    
        for i in nums2:
                if i in nums1 :
                    ans["ans2"] += 1
                    
        return [ans["ans1"],ans["ans2"]]
        