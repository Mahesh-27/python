class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self, name):
        if not self.seat():
            return False
        self.passenger.append(name)
        return True

    def seat(self):
        return self.capacity - len(self.passenger)


f = Flight(0)
a = ["a", "s", "d"]

for i in a:
    f.add_passenger(i)
