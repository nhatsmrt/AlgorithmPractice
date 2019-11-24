class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=Solution.key)

    @staticmethod
    def key(log: str) -> str:
        words = log.split(" ")
        if words[1].isnumeric():
            return "a"
        else:
            return "$" + log[len(words[0]):] + words[0]
    
