class RandomizedCollection:
    # Observation: order of stored elements does not matter

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = {}
        self.data = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        # Time Complexity: O(1)

        ret = False

        if val not in self.index:
            ret = True
            self.index[val] = set()

        self.index[val].add(len(self.data))
        self.data.append(val)

        return ret


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """

        # Time Complexity: O(1)
        if not self.index.get(val):
            return False

        last_occ = next(iter(self.index[val]))
        self.index[val].remove(last_occ)

        last_element = self.data[-1]

        if last_occ != len(self.data) - 1:
            self.index[last_element].remove(len(self.data) - 1)
            self.index[last_element].add(last_occ)
            self.data[last_occ] = last_element

        self.data.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        # Time Complexity: O(1)
        return self.data[random.randrange(len(self.data))]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
