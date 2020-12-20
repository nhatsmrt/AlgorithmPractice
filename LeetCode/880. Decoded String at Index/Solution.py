def is_digit(char):
    return "0" <= char and char <= "9"


class Node:
    def __init__(self, next=None):
        self.next = next
        self.repeat = 1
        self.free_text = []

    def compute_size(self):
        self.size = len(self.free_text)

        if self.next:
            self.size += self.next.repeated_size

        self.repeated_size = self.size * self.repeat

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        # Time and Space Complexity: O(|S|)

        i = 0
        node = Node()

        while i < len(S):
            if is_digit(S[i]):
                node.repeat = int(S[i])
                node.compute_size()
                node = Node(node)
            else:
                node.free_text.append(S[i])

            i += 1

        node.compute_size()
        K -= 1

        while True:
            K = K % node.size


            if node.next:
                if K < node.next.repeated_size:
                    node = node.next
                else:
                    return node.free_text[K - node.next.repeated_size]
            else:
                return node.free_text[K]
            
