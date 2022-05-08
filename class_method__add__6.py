class Box:
    def __init__(self, capacity: int):
        self.capacity = capacity

    def __add__(self, other):
        total = self.capacity + other.capacity
        return Box(total)


box1 = Box(10)
box2 = Box(20)
box3 = box1 + box2

print(box3.capacity)



