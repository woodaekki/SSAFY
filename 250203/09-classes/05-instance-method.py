class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1


c = Counter()
print(c.count)

c.increment()
print(c.count)

c2 = Counter()
c.increment()
print(c.count)
