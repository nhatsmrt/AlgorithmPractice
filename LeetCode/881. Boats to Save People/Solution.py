class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity O(sort(N))

        people.sort()
        ret = 0

        light = 0
        heavy = len(people) - 1

        while light <= heavy:
            ret += 1

            if light == heavy:
                light += 1
            else:
                if people[heavy] + people[light] <= limit:
                    light += 1
                    heavy -= 1
                else:
                    heavy -= 1


        return ret
        
