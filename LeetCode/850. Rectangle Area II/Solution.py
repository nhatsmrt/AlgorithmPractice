class Event:
    def __init__(self, value: int, ind: int, start: bool):
        self.value = value
        self.ind = ind
        self.start = start

    def __str__(self):
        return str(self.value) + "_" + str(self.ind) + "_" + str(self.start)

    def __repr__(self):
        return str(self.value) + "_" + str(self.ind) + "_" + str(self.start)

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MODULO = 1000000007
        vertical_events = []
        for i in range(len(rectangles)):
            vertical_events.append(Event(rectangles[i][0], i, True))
            vertical_events.append(Event(rectangles[i][2], i, False))

        vertical_events.sort(key=lambda ev: ev.value)

        total_area = 0
        considered = set()
        considered.add(vertical_events[0].ind)
        left = vertical_events[0].value
        for i in range(1, len(vertical_events)):
            horizontal_events = []
            delta_x = vertical_events[i].value - left

            if len(considered) > 0 and delta_x > 0:
                for r in considered:
                    horizontal_events.append(Event(rectangles[r][1], r, True))
                    horizontal_events.append(Event(rectangles[r][3], r, False))

                delta_y = 0
                horizontal_events.sort(key=lambda ev: ev.value)
                low = horizontal_events[0].value
                considered_hor = set()
                considered_hor.add(horizontal_events[0].ind)

                for j in range(1, len(horizontal_events)):
                    if horizontal_events[j].start:
                        considered_hor.add(horizontal_events[j].ind)
                    else:
                        considered_hor.remove(horizontal_events[j].ind)

                    if len(considered_hor) == 0:
                        delta_y += horizontal_events[j].value - low
                    elif len(considered_hor) == 1 and horizontal_events[j].start:
                        low = horizontal_events[j].value

                total_area += ((delta_x % MODULO) * (delta_y % MODULO)) % MODULO


            left = vertical_events[i].value
            if vertical_events[i].start:
                considered.add(vertical_events[i].ind)
            else:
                considered.remove(vertical_events[i].ind)

        return total_area % MODULO
