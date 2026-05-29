class Solution:
    def findMin(self, nums: List[int]) -> int:

        answer = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r) // 2

            if nums[l] < nums[r]:
                answer = min(answer, nums[l])
                break

            

            answer = min(answer, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1



        return answer
        
        