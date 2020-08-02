class MyHashSet:
    _MOD = 1001

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [[] for i in range(self._MOD)]


    def add(self, key: int) -> None:
        if not self.contains(key):
            self.data[key % self._MOD].append(key)


    def remove(self, key: int) -> None:
        if self.contains(key):
            self.data[key % self._MOD].remove(key)


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.data[key % self._MOD]



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
