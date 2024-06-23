class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Count the frequency of each element
        count = Counter(nums)

        # Step 2: Create an array of empty lists to act as buckets
        # The length of the bucket array should be len(nums) + 1 because the maximum frequency any number can 
        freq = [[] for _ in range(len(nums) + 1)]

        # Step 3: Fill the buckets
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Step 4: Gather the top k frequent elements from the buckets
        res = []
        for i in range(len(freq) - 1, 0, -1):  # Start from the end of the list
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                