class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mods = [0] * k
        for num in arr:
            mods[num % k] += 1

        for i in range(k):
            if i == (k - i) % k and mods[i] % 2 != 0:
                return False
            elif  i != (k - i) % k and mods[i] != mods[k - i]:
                return False

        return True

        
