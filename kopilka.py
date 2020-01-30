class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0

    def can_add(self, v):
        if self.current + v > self.capacity:
            return False
        else:
            return True

    def add(self, v):
        if self.can_add(v):
            self.current += v


m = MoneyBox(100)

m.add(9)
m.add(177)
print(m.current)