# https://leetcode.com/discuss/interview-question/304048/Google-onsite-question-Design-Text-Editor

from dataclasses import dataclass

@dataclass
class DataNode:
    char: str
    next: DataNode = None


class TextEditor:
    # Gap Buffer
    def __init__(self):
        self.left, self.right = None, None
        self.past_versions = []

    def move_cursor_left(self):
        # Time Complexity: O(1)
        if self.left:
            new_left = self.left.next
            new_right = DataNode(self.left.char, self.right)
            self.left, self.right = new_left, new_right

    def move_cursor_right(self):
        # Time Complexity: O(1)
        if self.right:
            new_right = self.right.next
            new_left = DataNode(self.right.char, self.left)
            self.left, self.right = new_left, new_right

    def insert_character(self, char: str):
        # Time Complexity: O(1)
        self.past_versions.append((self.left, self.right))
        self.left = DataNode(char, self.left)

    def backspace(self):
        # Time Complexity: O(1)
        if self.left:
            self.past_versions.append((self.left, self.right))
            self.left = self.left.next

    def undo(self):
        # Time Complexity: O(1)
        if self.past_versions:
            self.left, self.right = self.past_versions.pop()
