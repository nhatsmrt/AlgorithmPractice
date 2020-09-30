class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        # Time Complexity: O(1) initialization; O(1) per query
        # Total Space Complexity: O(Q)

        self.used = set()
        self.released = []
        self.max = maxNumbers
        self.max_used = -1
        self.next = Node(0)


    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.next.val == self.max:
            return -1

        ret = self.next.val

        if self.next.next:
            self.next = self.next.next
        else:
            # self.next points to max_used + 1
            self.next = Node(self.max_used + 2)

        self.max_used = max(self.max_used, ret)
        self.used.add(ret)

        return ret


    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number not in self.used


    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self.used:
            self.used.remove(number)
            self.released.append(number)

            cur_next = self.next
            self.next = Node(number, self.next)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
