class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest = 1

        curr_length = 1

        for i, n in enumerate(nums):
            
            if i > 0:
                if nums[i-1] == n - 1:
                    curr_length += 1
                    longest = max(longest, curr_length)
                elif nums[i-1] == n:
                    continue
                else:
                    curr_length = 1





        return longest