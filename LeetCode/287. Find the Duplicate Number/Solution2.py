class BloomFilter:
    def __init__(self):
        self.storage = [0 for _ in range(2097152)]
        self.hash_fns = [
            lambda x: ((x * 4414511) & 2097151),
            lambda x: ((x * 1341141) & 2097151)
        ]

    def add(self, value: int):
        for hash_fn in self.hash_fns:
            self.storage[hash_fn(value)] = 1

    def contains(self, value: int) -> bool:
        for hash_fn in self.hash_fns:
            if self.storage[hash_fn(value)] == 0:
                return False

        return True


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bf = BloomFilter()
        for value in nums:
            if bf.contains(value):
                return value
            bf.add(value)

        
