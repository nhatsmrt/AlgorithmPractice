class ComplementSet:
    def __init__(self, max_val: int):
        self.max_val = max_val
        self.missing = list(range(max_val, 0, -1))
        self.added = set()


    def add(self, value):
        self.added.add(value)

    def get_mex(self):
        while self.missing and self.missing[-1] in self.added:
            self.missing.pop()

        if self.missing:
            return self.missing[-1]

        return self.max_val + 1


class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        # Time and Space Complexity: O(N)

        children = {}
        root = 0
        self.path_to_one = []

        for node, par in enumerate(parents):
            if par >= 0:
                if par not in children:
                    children[par] = set()

                children[par].add(node)


        ret = [None] * len(parents)
        self.first_pass(root, children, nums, [])

        path_to_one_set = set(self.path_to_one)
        for node in range(len(parents)):
            if node not in path_to_one_set:
                ret[node] = 1

        comp_set = ComplementSet(len(parents))

        for i in range(len(self.path_to_one) - 1, -1, -1):
            self.second_pass(i, self.path_to_one, children, nums, comp_set, ret)

        return ret

    def first_pass(self, node, children, nums, path):
        # Goal: Determine path to node with value 1
        path.append(node)

        if nums[node] == 1:
            self.path_to_one = deepcopy(path)

        for child in children.get(node, []):
            self.first_pass(child, children, nums, path)

        path.pop()

    def add_values(self, node, children, nums, comp_set):
        comp_set.add(nums[node])

        for child in children.get(node, []):
            self.add_values(child, children, nums, comp_set)

    def second_pass(self, i, path_to_one, children, nums, comp_set, ret):
        comp_set.add(nums[path_to_one[i]])

        for child in children.get(path_to_one[i], []):
            if i == len(path_to_one) - 1 or path_to_one[i + 1] != child:
                self.add_values(child, children, nums, comp_set)

        ret[path_to_one[i]] = comp_set.get_mex()
