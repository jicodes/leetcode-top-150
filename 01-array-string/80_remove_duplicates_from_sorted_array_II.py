from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates in-place from a sorted array allowing at most two duplicates and returns the new length.
        :param nums: List[int] - The sorted list of numbers.
        :return: int - The new length of nums after removal of duplicates.
        """
        # Edge case: empty array
        if not nums:
            return 0

        # Pointer for the next position to place a unique element
        new_length = 1
        count = 1  # Count of occurrences for the current element

        # Iterate through each element starting from the second one
        for i in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[i] != nums[i - 1]:
                # Place the current element at the new_length index
                nums[new_length] = nums[i]
                new_length += 1
                count = 1  # Reset count for the new element
            elif count < 2:
                # If the current element is the same as the previous one and count is less than 2
                # Place the current element at the new_length index
                nums[new_length] = nums[i]
                new_length += 1
                count += 1

        return new_length
