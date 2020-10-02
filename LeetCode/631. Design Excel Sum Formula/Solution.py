class Cell:
    def __init__(self, r, c):
        self.r, self.c = r, c
        self.val = 0
        self.forward = set()
        self.backward = {}

    def recompute(self) -> int:
        self.val = 0

        for cell in self.backward:
            self.val += cell.val * self.backward[cell]

        return self.val

    def add_dependency(self, cell):
        self.backward[cell] = self.backward.get(cell, 0) + 1

    def clear_dependency(self):
        for cell in self.backward:
            cell.forward.remove(self)

        self.backward = {}

    def __repr__(self):
        return str((self.r, self.c, self.val))

class Excel:
    def __init__(self, H: int, W: str):
        self.H, self.W = H, W
        self.cells = {}


    def set(self, r: int, c: str, v: int) -> None:
        changed_cell = self.get_cell(r, c)
        changed_cell.clear_dependency() # clear backward dependency

        old_val = changed_cell.val
        changed_cell.val = v
        self._propagate(changed_cell, v - old_val)

    def get_cell(self, r: int, c: str) -> Cell:
        if (r, c) not in self.cells:
            self.cells[(r, c)] = Cell(r, c)

        return self.cells[(r, c)]

    def _propagate(self, changed_cell, delta):
        # Topological sort:
        back_connections = {}
        complete = [changed_cell]
        change_quantity = {changed_cell: delta}

        self._dfs(changed_cell, back_connections, set())

        while complete:
            cell = complete.pop()

            for next_cell in cell.forward:
                back_connections[next_cell] -= 1
                change_quantity[next_cell] = change_quantity[cell] * next_cell.backward[cell] + change_quantity.get(next_cell, 0) # propagate change

                if back_connections[next_cell] == 0:
                    next_cell.val += change_quantity[next_cell]
                    complete.append(next_cell)

    def _dfs(self, cell, back_connections, visited):
        for next_cell in cell.forward:
            back_connections[next_cell] = back_connections.get(next_cell, 0) + 1

            if next_cell not in visited:
                visited.add(next_cell)
                self._dfs(next_cell, back_connections, visited)

    def get(self, r: int, c: str) -> int:
        return self.get_cell(r, c).val

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        changed_cell = self.get_cell(r, c)
        changed_cell.clear_dependency()
        formulas = map(lambda form: form.split(":"), strs)

        for formula in formulas:
            min_row, min_col = int(formula[0][1:]), formula[0][0]
            max_row, max_col = int(formula[-1][1:]), formula[-1][0]

            for r in range(min_row, max_row + 1):
                for c_ind in range(ord(min_col), ord(max_col) + 1):
                    c = chr(c_ind)
                    depending_cell = self.get_cell(r, c)
                    changed_cell.add_dependency(depending_cell)
                    depending_cell.forward.add(changed_cell)

        old_val = changed_cell.val
        new_val = changed_cell.recompute()
        self._propagate(changed_cell, new_val - old_val)
        return new_val


# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
