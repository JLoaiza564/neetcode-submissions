class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeroes = 0
        total_product = 1

        for n in nums:
            if n == 0:
                num_zeroes += 1 
            else:
                total_product *= n

        products = [0] * len(nums)

        if num_zeroes > 1:
            return products
        elif num_zeroes == 1:
            products[nums.index(0)] = total_product
            return products
        
        for i, n in enumerate(nums):
            products[i] = total_product // n




        return products

                