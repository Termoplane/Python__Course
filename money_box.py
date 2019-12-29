class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.money = 0    
    def can_add(self, v):
        if self.money + v < self.capacity:
            return True
        else:
            return False
    def add(self, v):
        if self.can_add(v) == True:
            self.money += v
        else:
            return False 