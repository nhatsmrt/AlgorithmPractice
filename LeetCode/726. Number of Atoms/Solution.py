class ParseNode:
    def __init__(self, atom: str=None, mult_factor: int=1):
        self.atom, self.mult_factor = atom, mult_factor
        self.children = []


def parse_atom(formula, start):
    end = start

    while end < len(formula) and ((formula[end].isupper() and end == start) or formula[end].islower()):
        end += 1

    return formula[start:end], end

def parse_int(formula, start):
    end = start

    while end < len(formula) and formula[end].isdigit():
        end += 1

    ret = 1 if start == end else int(formula[start:end])
    return ret, end


def parse(formula: str, i: int, par_node: ParseNode):
    if i == len(formula): # end of string
        return i

    node = ParseNode()
    par_node.children.append(node)

    if formula[i] == '(':
        # non-leaf node:
        end = i + 1

        while formula[end] != ')':
            end = parse(formula, end, node)

        end += 1 # )
    else: # a leaf/atom node
        atom, end = parse_atom(formula, i)
        node.atom = atom


    mult_factor, ret = parse_int(formula, end)
    node.mult_factor = mult_factor

    return ret


def count_atoms(node, cnter, mult_factor):
    mult_factor *= node.mult_factor

    if node.atom:
        cnter[node.atom] += mult_factor
    else:
        for child in node.children:
            count_atoms(child, cnter, mult_factor)


def cnter_to_str(cnter: Counter) -> str:
    ret = []
    for atom in sorted(cnter.keys()):
        ret.append(atom)
        cnt = cnter[atom]

        if cnt > 1:
            ret.append(str(cnt))

    return "".join(ret)


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Time Complexity: O(S + A log A)
        # Space Complexity: O(S + A)

        # Where S is the length of formula
        # and A is the size of atom alphabet

        root = ParseNode()

        end = 0

        while end < len(formula):
            end = parse(formula, end, root)
        cnter = Counter()

        count_atoms(root, cnter, 1)

        return cnter_to_str(cnter)
