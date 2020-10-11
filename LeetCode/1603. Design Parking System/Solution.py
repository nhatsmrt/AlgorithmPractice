class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.counter = collections.Counter()
        self.counter[1] = big
        self.counter[2] = medium
        self.counter[3] = small

    def addCar(self, carType: int) -> bool:
        if self.counter[carType]:
            self.counter[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
