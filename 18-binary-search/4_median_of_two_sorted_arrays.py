# Approch 1: Merge and Sort
# from typing import List


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         merged = []
#         i, j = 0, 0

#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] < nums2[j]:
#                 merged.append(nums1[i])
#                 i += 1
#             else:
#                 merged.append(nums2[j])
#                 j += 1

#         while i < len(nums1):
#             merged.append(nums1[i])
#             i += 1

#         while j < len(nums2):
#             merged.append(nums2[j])
#             j += 1

#         mid = len(merged) // 2
#         if len(merged) % 2 == 0:
#             return (merged[mid - 1] + merged[mid]) / 2
#         else:
#             return merged[mid]

# Approach 2: Binary Search
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Swap to ensure nums1 is the smaller array
        
        m, n = len(nums1), len(nums2)  # Lengths of the two arrays
        left, right = 0, m  # Binary search range in nums1
        
        while left <= right:
            partition1 = left + (right - left) // 2  # Partition index in nums1
            partition2 = (m + n + 1) // 2 - partition1  # Partition index in nums2
            
            # Handle the edge cases where partition index is at the boundaries
            leftMax1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]  # Left max in nums1
            rightMin1 = float('inf') if partition1 == m else nums1[partition1]  # Right min in nums1
            
            leftMax2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]  # Left max in nums2
            rightMin2 = float('inf') if partition2 == n else nums2[partition2]  # Right min in nums2
            
            # Check if the partitions are correct
            if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
                # If the combined array length is even, return the average of the two middle values
                if (m + n) % 2 == 0:
                    return (max(leftMax1, leftMax2) + min(rightMin1, rightMin2)) / 2
                else:  # If the combined array length is odd, return the middle value
                    return max(leftMax1, leftMax2)
            elif leftMax1 > rightMin2:  # Move partition1 to the left
                right = partition1 - 1
            else:  # Move partition1 to the right
                left = partition1 + 1