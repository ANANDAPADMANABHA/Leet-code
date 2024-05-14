class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        def is_arithmetic(seq):
            if len(seq) < 2:
                return False
            diff = seq[1] - seq[0]
            for i in range(2, len(seq)):
                if seq[i] - seq[i - 1] != diff:
                    return False
            return True

        result = []
        for i in range(len(l)):
            subarray = nums[l[i]:r[i] + 1]
            subarray.sort()
            result.append(is_arithmetic(subarray))

        return result
