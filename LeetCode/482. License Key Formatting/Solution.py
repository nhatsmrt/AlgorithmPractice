class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        components = S.split("-")
        characters = []
        for comp in components:
            for char in comp:
                characters.append(char.upper())
        ret = []
        for i in range(len(characters)):
            ret.append(characters[i])
            if i < len(characters) - 1 and (len(characters) - i - 1) % K == 0:
                ret.append("-")
        return "".join(ret)
