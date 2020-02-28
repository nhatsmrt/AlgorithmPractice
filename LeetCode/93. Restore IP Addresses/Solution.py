class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Definition of valid IP address:
        # 1. The length of the ip without '.' should be equal to the length of s;
        # 2. The digit order of ip should be same as the digit order of s;
        # 3. Each part separated by the '.' should not start with '0' except only '0';
        # 4. Each part separared by the '.' should not larger than 255;

        if len(s) > 12:
            return []
        ret = []

        self.backtrack(s, [[]], 0, ret)

        return ret

    def backtrack(self, s: str, components: List[List[str]],
                    i: int, ret: List[str]):
        if i == len(s):
            # done
            if len(components) == 4:
                if self.is_valid(components[-1]):
                    components_str = [''.join(component) for component in components]
                    ret.append('.'.join(components_str))
        else:
            # Option 1: finish current component, make a new component:
            if self.is_valid(components[-1]):
                new_component = [s[i]]
                components.append(new_component)
                self.backtrack(s, components, i + 1, ret)
                # unchoose:
                components.pop()

            # Option 2: add the current digit to the current component
            components[-1].append(s[i])
            self.backtrack(s, components, i + 1, ret)
            # unchoose
            components[-1].pop()

    def is_valid(self, component: List[str]):
        if len(component) == 0:
            return False

        if component[0] == "0":
            return len(component) == 1

        val = int(''.join(component))
        return val <= 255
