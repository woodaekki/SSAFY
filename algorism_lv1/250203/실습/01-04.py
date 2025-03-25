class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f"Width: {self.width}")
        print(f"height: {self.height}")
        print(f"area: {self.width * self.height}")
        print(f"perimeter: {2 * (self.width + self.height)}")
        

shape1 = Shape(5, 3)
shape1.print_info()