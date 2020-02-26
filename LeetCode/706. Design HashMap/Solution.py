class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.MAX_ITERATON = 1000
        self.data_size = 8192
        self.update_hash()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.put_helper(key, value, 0)

    def put_helper(self, key: int, value: int, iteration: int):
        if iteration > self.MAX_ITERATON:
            self.rebuild()
            self.put_helper(key, value, 0)
        else:
            ind = self.hash_fn1(key)
            if self.data_1[ind] is None or self.data_1[ind][0] == key:
                self.data_1[ind] = (key, value)
            else:
                ind = self.hash_fn2(key)
                if self.data_2[ind] is None or self.data_2[ind][0] == key:
                    self.data_2[ind] = (key, value)
                else:
                    old_key, old_vl = self.data_2[ind]
                    self.data_2[ind] = (key, value)
                    self.put_helper(old_key, old_vl, iteration + 1)

    def rebuild(self):
        old_data = []
        for i in range(len(self.data_1)):
            if self.data_1[i] is not None:
                old_data.append(self.data_1[i])

        for i in range(len(self.data_2)):
            if self.data_2[i] is not None:
                old_data.append(self.data_2[i])

        self.data_size *= 2
        self.update_hash()

        for data in old_data:
            key, value = data
            self.put_helper(key, value, 0)

    def update_hash(self):
        self.hash_fn1 = lambda x: (x * 12163) % self.data_size
        self.hash_fn2 = lambda x: (x * 12329) % self.data_size

        self.data_1 = [None for i in range(self.data_size)]
        self.data_2 = [None for i in range(self.data_size)]

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

        ind = self.hash_fn1(key)
        if self.data_1[ind] is not None and self.data_1[ind][0] == key:
            return self.data_1[ind][1]

        ind = self.hash_fn2(key)
        if self.data_2[ind] is not None and self.data_2[ind][0] == key:
            return self.data_2[ind][1]

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        ind = self.hash_fn1(key)
        if self.data_1[ind] is not None and self.data_1[ind][0] == key:
            self.data_1[ind] = None
        else:
            ind = self.hash_fn2(key)
            if self.data_2[ind] is not None and self.data_2[ind][0] == key:
                self.data_2[ind] = None




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
