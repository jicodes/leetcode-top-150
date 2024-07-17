import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize a min-heap
        min_heap = []

        # Iterate through each number in the array
        for num in nums:
            # Push the current number onto the heap
            heapq.heappush(min_heap, num)
            # If the heap size exceeds k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # The root of the heap is the k-th largest element
        return min_heap[0]
