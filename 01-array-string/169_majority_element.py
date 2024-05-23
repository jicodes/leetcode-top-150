from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        # Creating a defaultdict with default value as int (default value of 0)
        m = defaultdict(int)

        for num in nums:
            m[num] += 1

        for key, value in m.items():
            if value > n // 2:
                return key

        return 0


# from typing import List


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         """
#         Finds the majority element in the array.
#         :param nums: List[int] - The list of numbers.
#         :return: int - The majority element.
#         """
#         count = 0
#         candidate = None

#         # Boyer-Moore Voting Algorithm
#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += 1 if num == candidate else -1

#         return candidate
