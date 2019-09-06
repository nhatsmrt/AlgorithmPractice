class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller = []
        self.larger = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.smaller) + len(self.larger) == 0:
            heapq.heappush(self.larger, num)
        else:
            cur_median = self.findMedian()
            if num < cur_median:
                heapq.heappush(self.smaller, -num)
            else:
                heapq.heappush(self.larger, num)

            if len(self.smaller) > len(self.larger) + 1:
                heapq.heappush(self.larger, -self.smaller[0])
                heapq.heappop(self.smaller)
            elif len(self.larger) > len(self.smaller) + 1:
                heapq.heappush(self.smaller, -self.larger[0])
                heapq.heappop(self.larger)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.smaller) == len(self.larger):
            return (-self.smaller[0] + self.larger[0]) / 2
        elif len(self.smaller) < len(self.larger):
            return self.larger[0]
        else:
            return -self.smaller[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
