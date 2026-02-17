# Your code should include:
# A class called Rectangle
# width and height attributes with property decorators
# A get_area method that calculates the area of the rectangle
# Appropriate error handling for non-positive width and height values

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError('Witdh can not be negative')
        self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError('Height can not be negative')
        self._height = height

    @property
    def area(self):
        return (self.height + self.width)**2