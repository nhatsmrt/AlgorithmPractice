class IxPriorityQueue:
    def __init__(self, data):
        self.data = [(data[i], i) for i in data]
        heapq.heapify(self.data)

        self.index = {}
        for ind, (value, node_ind) in enumerate(self.data):
            self.index[node_ind] = ind

    def pop(self) -> int:
        dist, node_ind = self.data[0]

        self.data[0] = self.data[-1]
        self.index[self.data[0][1]] = 0
        self.data.pop()
        self.index.pop(node_ind)

        self.sift_down(0)

        return dist, node_ind

    def get_val(self, node_ind) -> int:
        return self.data[self.index[node_ind]][0]

    def decrease_val(self, node_ind: int, new_val: int):
        cur_ind = self.index[node_ind]
        self.data[cur_ind] = (new_val, node_ind)
        self.sift_up(cur_ind)

    def sift_down(self, ind: int):
        left_ind = ind * 2 + 1
        right_ind = ind * 2 + 2

        child_ind = None

        if right_ind < len(self.data):
            if self.data[left_ind][0] < self.data[right_ind][0]:
                child_ind = left_ind
            else:
                child_ind = right_ind
        elif left_ind < len(self.data):
            child_ind = left_ind

        if child_ind is not None and self.data[child_ind][0] < self.data[ind][0]:
            self.swap(ind, child_ind)
            self.sift_down(child_ind)

    # sifting up:
    def sift_up(self, ind: int):
        par_ind = (ind - 1) // 2
        if ind >= 1 and self.data[par_ind][0] > self.data[ind][0]:
            self.swap(ind, par_ind)
            self.sift_up(par_ind)

    def swap(self, ind1, ind2):
        node_ind1 = self.data[ind1][1]
        node_ind2 = self.data[ind2][1]

        tmp = self.data[ind1]
        self.data[ind1] = self.data[ind2]
        self.data[ind2] = tmp

        self.index[node_ind1] = ind2
        self.index[node_ind2] = ind1

    def __len__(self): return len(self.data)


class Solution:
    _MOD = 1000000007

    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        # Time Complexity: O((V + E) log V)
        # Space Complexity: O(V + E)

        d_to_n = {}
        INF = 10000000000
        cur_d = {i: INF for i in range(1, n + 1)}
        cur_d[n] = 0
        cur_d_pq = IxPriorityQueue(cur_d)
        adj_lists = {i: set() for i in range(1, n + 1)}

        for (node1, node2, edge_weight) in edges:
            adj_lists[node1].add((node2, edge_weight))
            adj_lists[node2].add((node1, edge_weight))

        while cur_d_pq:
            node_dist, node = cur_d_pq.pop()

            d_to_n[node] = node_dist
            for (neighbor, edge_weight) in adj_lists[node]:
                if neighbor in cur_d_pq.index and node_dist + edge_weight < cur_d_pq.get_val(neighbor):
                    cur_d_pq.decrease_val(neighbor, node_dist + edge_weight)

        self.dp = {}
        self.d_to_n = d_to_n
        self.adj_lists = {i: {j for (j, _) in adj_lists[i] if d_to_n[j] > d_to_n[i]} for i in range(1, n + 1)}
        return self.num_paths(n)

    def num_paths(self, cur: int) -> int:
        if cur == 1:
            return 1

        if cur in self.dp:
            return self.dp[cur]

        ret = 0
        for neighbor in self.adj_lists[cur]:
            ret += self.num_paths(neighbor)
            ret %= self._MOD

        self.dp[cur] = ret
        return ret
