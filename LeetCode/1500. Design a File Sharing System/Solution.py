from sortedcontainers import SortedSet


class FileSharing:

    def __init__(self, m: int):
        self.owned_by = {}
        self.user = {}
        self.max_id_assigned = 0
        self.released = SortedSet()

    def get_user_id(self) -> int:
        if len(self.released):
            return self.released.pop(0)

        self.max_id_assigned += 1
        return self.max_id_assigned

    def join(self, ownedChunks: List[int]) -> int:
        ret = self.get_user_id()

        for chunk in ownedChunks:
            if chunk not in self.owned_by:
                self.owned_by[chunk] = set()

            self.owned_by[chunk].add(ret)

        self.user[ret] = set(ownedChunks)
        return ret

    def leave(self, userID: int) -> None:
        for chunk in self.user[userID]:
            self.owned_by[chunk].remove(userID)

        self.user.pop(userID)
        self.released.add(userID)


    def request(self, userID: int, chunkID: int) -> List[int]:
        ret = sorted(self.owned_by.get(chunkID, []))

        if ret:
            self.user[userID].add(chunkID)
            self.owned_by[chunkID].add(userID)

        return ret



# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)
