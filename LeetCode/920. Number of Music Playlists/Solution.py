class Solution:
    MOD = 1000000007

    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        # Time and Space Complexity: O(NL)
        self.dp = {}
        return self.build_playlist(N, L, N, L, K)

    def build_playlist(self, n: int, l: int, N: int, L: int, K: int) -> int:
        # returns number of playlist of length l, builds from n unique songs
        # such that a song can only be played again only if K other songs have been played
        if (n, l) in self.dp:
            return self.dp[(n, l)]

        if l == 0 or n == 0:
            ret = 1 if (l == 0 and n == 0) else 0
        else:
            # suppose we have build a playlist of length l - 1
            # case 1: we have used n - 1 unique songs, and need to choose another unique song
            ret = self.build_playlist(n - 1, l - 1, N, L, K) * (N + 1 - n)
            ret %= self.MOD

            # case 2: we have already used n unique songs, and need to choose one of the
            # songs other than the last K songs used
            if n > K:
                ret += (self.build_playlist(n, l - 1, N, L, K) * (n - K)) % self.MOD
                ret %= self.MOD

        self.dp[(n, l)] = ret
        return ret
