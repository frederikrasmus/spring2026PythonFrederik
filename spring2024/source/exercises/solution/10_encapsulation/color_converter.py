class Color:
    def __init__(self, r, g, b):
            self.r = r
            self.g = g
            self.b = b

    @property
    def hex(self):
        return f'#{hex(self.r)[2:]}{hex(self.g)[2:]}{hex(self.b)[2:]}'
    
