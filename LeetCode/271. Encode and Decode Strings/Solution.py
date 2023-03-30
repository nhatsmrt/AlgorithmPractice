class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # Time and Space Complexity: O(N)
        def fixed_len(word: str):
            str_len = str(len(word))
            ret = ["0"] * (3 - len(str_len))
            ret.append(str_len)
            return "".join(ret)

        strs_len = map(fixed_len, strs)
        strs_with_len = [
            str_len + word for str_len, word in zip(strs_len, strs)
        ]

        return "".join(strs_with_len)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # Time and Space Complexity: O(N)
        i = 0
        ret = []

        while i < len(s):
            str_len = int(s[i:i+3])
            i += 3
            word = []
            for _ in range(str_len):
                word.append(s[i])
                i += 1

            ret.append("".join(word))

        return ret



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
