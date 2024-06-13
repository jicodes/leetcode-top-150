from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * length
        # `[1] * length` creates a list containing `1` repeated `length` times.

        # Calculate products of elements to the left of each element
        for i in range(1, length):
            products[i] = products[i - 1] * nums[i - 1]

        right = nums[-1]

        # Multiply the products with the products of elements to the right
        for i in range(length - 2, -1, -1):
            products[i] *= right
            right *= nums[i]

        return products
