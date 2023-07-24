class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self):
        return self.width

    def set_height(self):
        return self.height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = ((2*self.width)+(2*self.height))
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width**2)+(self.height**2))**0.5
        return diagonal

    def get_picture():
        picture = 0
        return picture

    def get_amount_inside():
        shape = 0
        return shape

rect = Rectangle(5, 10)
print(rect.get_diagonal())