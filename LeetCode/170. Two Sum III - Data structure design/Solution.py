class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cnter = collections.Counter()


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.cnter[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for first in self.cnter:
            if value - first != first and (value - first) in self.cnter:
                return True
            elif value - first == first and self.cnter[first] > 1:
                return True

        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
