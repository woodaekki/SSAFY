class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


c = Counter()
print(c.count)  # 0
c.increment()
print(c.count)  # 1

c2 = Counter()
c.increment()
print(c2.count)  # 0
print(c.count)  # 2
