class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()

        l = 0
        while l < len(nums):
            m = l + 1
            r = len(nums) - 1

            while m < r:
                curr_sum = nums[l] + nums[m] + nums[r]

                if curr_sum > 0:
                    r -= 1
                elif curr_sum < 0:
                    m += 1
                elif nums[l] + nums[m] + nums[r] == 0:
                    result.append([nums[l], nums[m], nums[r]])

                    m += 1
                    while nums[m] == nums[m-1] and m < r:
                        m += 1
            
            l += 1
            while l < len(nums) and  nums[l] == nums[l-1]:
                l += 1

        return result
