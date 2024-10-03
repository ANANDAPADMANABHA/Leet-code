class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []  # To store all the subsets

        def backtrack(start, path):
            # Add the current subset to the result
            result.append(path[:])
            
            # Iterate over all remaining elements
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])
                
                # Recursively generate subsets including nums[i]
                backtrack(i + 1, path)
                
                # Backtrack, remove nums[i] from the subset
                path.pop()

        # Start the backtracking process with an empty path (subset)
        backtrack(0, [])
        
        return result
