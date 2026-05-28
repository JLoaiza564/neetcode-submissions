class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = [0] * len(nums)

        running_product = 1
        for i in range(len(nums)):
            products[i] = running_product
            running_product *= nums[i]

        running_product = 1

        for i in range(len(nums)-1, -1, -1):
            products[i] *= running_product
            running_product *= nums[i]

        return products
