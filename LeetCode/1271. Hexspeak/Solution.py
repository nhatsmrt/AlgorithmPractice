class Solution:
    def toHexspeak(self, num: str) -> str:
        hex_rep = hex(int(num))[2:].replace("1", "I").replace("0", "O").upper()

        if list(filter(lambda char: char not in "ABCDEFIO", hex_rep)):
            return "ERROR"
        else:
            return hex_rep
