
class IxPQ:
    def __init__(self):
        self.data = []
        self.k2i = {}
        self.i2k = []

    def swap(self, ind1, ind2):
        val1, val2 = self.data[ind1], self.data[ind2]
        key1, key2 = self.i2k[ind1], self.i2k[ind2]

        self.data[ind2] = val1
        self.data[ind1] = val2

        self.i2k[ind1] = key2
        self.i2k[ind2] = key1

        self.k2i[key1] = ind2
        self.k2i[key2] = ind1

    def sift_up(self, pos):
        if pos:
            par = (pos - 1) // 2

            if self.data[par] > self.data[pos]:
                self.swap(par, pos)
                self.sift_up(par)

    def sift_down(self, pos):
        left = pos * 2 + 1
        right = pos * 2 + 2

        child = None

        if right < len(self.data):
            child = left if self.data[left] < self.data[right] else right
        elif left < len(self.data):
            child = left

        if child and self.data[pos] > self.data[child]:
            self.swap(pos, child)
            self.sift_down(child)

    def insert(self, key, priority):
        self.data.append(priority)
        self.k2i[key] = len(self.data) - 1
        self.i2k.append(key)

        self.sift_up(len(self.data) - 1)

    def remove_min(self):
        return self.remove_key(self.i2k[0])

    def remove_key(self, key):
        if key in self.k2i:
            ind = self.k2i[key]

            ret_priority = self.data[ind]
            self.swap(ind, len(self.data) - 1)
            self.k2i.pop(self.i2k[-1])
            self.data.pop()
            self.i2k.pop()


            if ind < len(self.data) and ind > 0 and self.data[(ind - 1) // 2] > self.data[ind]:
                self.sift_up(ind)
            else:
                self.sift_down(ind)

            return key, ret_priority

    def __len__(self):
        return len(self.data)


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        actions = []

        for i, (start, end) in enumerate(events):
            actions.append((start, 0, end, i))
            actions.append((end + 1, 1, end, i))

        actions.sort()
        cur_time = 0
        action_ind = 0

        ret = 0
        available_events = IxPQ()

        while action_ind < len(actions):
            if action_ind < len(actions) and (actions[action_ind][0] <= cur_time or (not available_events)):
                timestamp, is_end, associated_end, event_ind = actions[action_ind]

                if is_end:
                    available_events.remove_key(event_ind)
                else:
                    available_events.insert(event_ind, associated_end)


                cur_time = max(cur_time, timestamp)
                action_ind += 1
            else:
                available_events.remove_min()
                cur_time += 1
                ret += 1

        return ret
