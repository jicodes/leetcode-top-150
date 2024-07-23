import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        # If either of the input arrays is empty, return an empty list
        if not nums1 or not nums2:
            return []
        
        # Initialize a min-heap to keep track of pairs and their sums
        min_heap = []
        # Push the first element of nums2 paired with each element of nums1 into the heap
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        # Initialize a result list to store the k smallest pairs
        result = []
        # While the heap is not empty and we have not found k pairs
        while min_heap and len(result) < k:
            # Extract the smallest pair from the heap
            curr_sum, i, j = heapq.heappop(min_heap)
            # Append the extracted pair to the result list
            result.append((nums1[i], nums2[j]))
            
            # If there are more elements in nums2 for the current nums1[i], push the next pair into the heap
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return result
