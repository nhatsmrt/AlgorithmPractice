class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.last_renewed = {}
        self.ttl = timeToLive


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.last_renewed[tokenId] = currentTime


    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.last_renewed:
            if currentTime - self.last_renewed[tokenId] < self.ttl:
                self.last_renewed[tokenId] = currentTime
            else:
                self.last_renewed.pop(tokenId)


    def countUnexpiredTokens(self, currentTime: int) -> int:
        ret = 0
        removed = []

        for tokenId in self.last_renewed:
            if currentTime - self.last_renewed[tokenId] < self.ttl:
                ret += 1
            else:
                removed.append(tokenId)

        for tokenId in removed:
            self.last_renewed.pop(tokenId)
        return ret



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
