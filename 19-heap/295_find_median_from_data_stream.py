import heapq


class MedianFinder:
    def __init__(self):
        # Min-heap to store the larger half of the numbers
        self.top = []
        # Max-heap to store the smaller half of the numbers (as negative values)
        self.bottom = []

    def addNum(self, num: int) -> None:
        # Add the new number to the max-heap (bottom) as a negative value
        heapq.heappush(self.bottom, -num)

        # Move the largest element from bottom to top to balance the heaps
        heapq.heappush(self.top, -heapq.heappop(self.bottom))

        # Balance the sizes of the heaps
        if len(self.top) > len(self.bottom):
            heapq.heappush(self.bottom, -heapq.heappop(self.top))

    def findMedian(self) -> float:
        # If the heaps are of equal size, the median is the average of the two middle values
        if len(self.bottom) == len(self.top):
            return (self.top[0] - self.bottom[0]) / 2.0

        # If bottom heap has more elements, the median is the root of bottom heap
        return -self.bottom[0]


# Example usage:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
