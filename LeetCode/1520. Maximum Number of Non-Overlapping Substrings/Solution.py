class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # Time and Space Complexity: O(N)

        # Idea: Represent the string as a graph, where each node is a character in the string
        # There is an edge from node u to node v if the char of v occurs between
        # the first and the last occurence of the char of u

        # Now note that if we pick the char corresponding to a node u
        # then we cannot pick any node that it can reach.
        # However, there might be cycles, complicating the selection process.

        # Use Kosaraju's algorithm to find strongly connected components (SCCs) of this graph
        # then collapse it into a directed acyclic graph (DAG) of SCCs

        # The problem becomes selecting the maximum number of nodes (i.e SCCs) in this DAG
        # such that: if we pick a node u then we cannot pick any of its descendants

        # So selecting the node with no out-neighbors is optimal
        # both in the number of nodes selected and the total length of the resulting strings.

        index = {}

        for i, char in enumerate(s):
            if char not in index:
                index[char] = (i, i)
            else:
                index[char] = (index[char][0], i)


        out_edges = {char: set() for char in index}
        in_edges = {char: set() for char in index}

        for char in index:
            for i in range(index[char][0], index[char][1] + 1):
                if s[i] != char:
                    out_edges[char].add(s[i])
                    in_edges[s[i]].add(char)

        # perform Kosaraju's algorithm

        # first DFS pass:
        finished = []
        visited = {char: False for char in index}

        for node in index:
            if not visited[node]:
                self.dfs(node, out_edges, visited, finished)

        # second DFS pass:
        assigned = {char: None for char in index}

        for node in reversed(finished):
            # consider node in reversed finished time
            if not assigned[node]:
                self.assign(node, node, in_edges, assigned)


        # Collapse the graph into a DAG of SCCs:
        node_boundary = {}
        dag = {}

        for node in assigned:
            if assigned[node] not in dag:
                dag[assigned[node]] = set()

            if assigned[node] not in node_boundary:
                node_boundary[assigned[node]] = index[assigned[node]]

            cur_first, cur_last = node_boundary[assigned[node]]
            node_boundary[assigned[node]] = (min(index[node][0], cur_first), max(index[node][1], cur_last))

        for node in assigned:
            for neighbor in out_edges[node]:
                root1 = assigned[node]
                root2 = assigned[neighbor]

                if root1 != root2:
                    dag[root1].add(root2)

        # select nodes in the DAG without out-neighbors:
        ret = []
        for node in dag:
            if not len(dag[node]):
                ret.append(s[node_boundary[node][0]:node_boundary[node][1] + 1])

        return ret


    def dfs(self, node, adj_lists, visited, finished):
        visited[node] = True

        for neighbor in adj_lists[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj_lists, visited, finished)

        finished.append(node)

    def assign(self, node, root, adj_lists, assigned):
        assigned[node] = root

        for neighbor in adj_lists[node]:
            if not assigned[neighbor]:
                self.assign(neighbor, root, adj_lists, assigned)
