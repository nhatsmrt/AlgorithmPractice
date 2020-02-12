class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks);

        ret = 0
        while len(sticks) > 1:
            num1 = heapq.heappop(sticks)
            num2 = heapq.heappop(sticks)
            num = num1 + num2
            ret += num
            heapq.heappush(sticks, num)

        return ret
        
