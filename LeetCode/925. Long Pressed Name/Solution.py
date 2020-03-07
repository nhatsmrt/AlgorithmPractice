from typing import Tuple, List


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_rle = self.rle(name)
        typed_rle = self.rle(typed)

        if len(name_rle) != len(typed_rle):
            return False

        for i in range(len(name_rle)):
            if name_rle[i][0] != typed_rle[i][0] or typed_rle[i][1] < name_rle[i][1]:
                return False

        return True

    def rle(self, text: str) -> List[Tuple[str, int]]:
        ret = []

        start = 0
        for i in range(len(text)):
            if text[i] != text[start]:
                ret.append((text[start], i - start))
                start = i

        ret.append((text[start], len(text) - start))
        return ret
        
