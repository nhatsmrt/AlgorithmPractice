class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = minutes * 6
        hour_angle = (hour % 12 + minutes / 60) * 30

        return min(abs(hour_angle - min_angle), 360 -abs(hour_angle - min_angle))
