class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0


        answer = 1

        nums = set(nums)

        for n in nums:
            if n-1 not in nums:
                curr_length = 1
                while n + curr_length in nums:
                    curr_length += 1
                    answer = max(answer, curr_length)


        print(nums)

        return answer