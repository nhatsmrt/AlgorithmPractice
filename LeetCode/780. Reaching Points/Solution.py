class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # Idea 1: work backwards from (tx, ty)
        # Idea 2: if tx > ty, then previous step must be (tx - ty, ty)
        # Idea 3: Spped up by combining multiple steps: (tx % ty, ty)
        # Exception: when tx == sx (or ty == sy), check if we can obtain sx (or sy)
        # Time Complexity: O(log(max(tx, ty)))
        while tx >= sx and ty >= sy:
            if tx == sx and (ty - sy) % sx == 0:
                return True
            if ty == sy and (tx - sx)  % sy == 0:
                return True

            if ty > tx:
                ty %= tx
            else:
                tx %= ty

        return False

        
