"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Time and Space Complexity: O(N)

        index = {}

        for employee in employees:
            index[employee.id] = employee

        def compute(employee):
            ret = employee.importance

            for subordinate in employee.subordinates:
                ret += compute(index[subordinate])

            return ret

        return compute(index[id])
