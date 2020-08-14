class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = self.process(version1)
        version2_list = self.process(version2)


        for pos in range(min(len(version1_list), len(version2_list))):
            if version1_list[pos] < version2_list[pos]:
                return -1
            elif version1_list[pos] > version2_list[pos]:
                return 1

        if len(version1_list) < len(version2_list) and sum(version2_list[len(version1_list):]) > 0:
            return -1
        elif len(version1_list) > len(version2_list) and sum(version1_list[len(version2_list):]) > 0:
            return 1

        return 0

    def process(self, version: str) -> List[int]:
        return list(map(int, version.split(".")))
        
