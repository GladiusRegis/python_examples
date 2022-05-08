class Box:
    def __init__(self, capacity: int):
        self.capacity = capacity

    def __eq__(self, other):
        return self.capacity == other.capacity


class Box1:
    def __init__(self, capacity: int):
        self.capacity = capacity


box1 = Box(10)
box2 = Box(10)
print(box1 == box2)
# True

box1 = Box1(10)
box2 = Box1(10)
print(box1 == box2)
# False
