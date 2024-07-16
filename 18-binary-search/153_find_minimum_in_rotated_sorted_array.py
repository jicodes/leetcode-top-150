class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1  # Initialize pointers

        while left < right:
            mid = left + (right - left) // 2  # Calculate mid to avoid overflow
            if nums[mid] > nums[right]:  # Minimum is in the right half
                left = mid + 1
            else:  # Minimum is in the left half or at mid
                right = mid

        return nums[left]  # Left points to the minimum element
