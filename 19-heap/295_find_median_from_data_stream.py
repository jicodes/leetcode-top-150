import heapq


class MedianFinder:
    def __init__(self):
        # Min-heap to store the larger half of the numbers
        self.large = []
        # Max-heap to store the smaller half of the numbers (as negative values)
        self.small = []

    def addNum(self, num: int) -> None:
        # Add the new number to the max-heap (small) as a negative value
        heapq.heappush(self.small, -num)

        # Move the largest element from small to large to balance the heaps
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance the sizes of the heaps
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # If the heaps are of equal size, the median is the average of the two middle values
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0

        # If small heap has more elements, the median is the root of small heap
        return -self.small[0]


# Example usage:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
