class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        for i, n in enumerate(nums):
            product = 1
            for j, n in enumerate(nums):
                if i != j:
                    product *= n
            products.append(product)

        return products
                