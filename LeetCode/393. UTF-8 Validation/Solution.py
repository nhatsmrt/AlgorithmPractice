class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        self.masks = [(1 << i) for i in range(7, -1, -1)]
        i = 0

        while i < len(data):
            if (self.masks[0] & data[i]) == 0:
                # num byte = 1
                i += 1
            else:
                num_byte = self.compute_num_byte(data[i])
                if num_byte == 1 or num_byte > 4:
                    return False
                if i + num_byte > len(data):
                    return False

                for j in range(i + 1, i + num_byte):
                    if not self.proper_byte(data[j]):
                        return False
                i += num_byte

        return True

    def compute_num_byte(self, num: int) -> int:
        i = 0
        while i < 8 and (num & self.masks[i]) > 0:
            i += 1
        return i

    def proper_byte(self, num) -> bool:
        return (num & self.masks[0]) > 0 and (num & self.masks[1]) == 0
