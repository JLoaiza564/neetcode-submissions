class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i, n in enumerate(nums):
            if target - n in seen:
                return [nums.index(target-n), i]
            else:
                seen.add(n)