from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # Ensure k is within the range [0, n)

        # Handle right rotations
        if k > 0:
            i = n - k
            nums[:] = nums[i:] + nums[:i]
