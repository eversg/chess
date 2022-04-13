import Figure

class Field:
    """single gray or white game spot with properties"""
    def __init__(self, image,x,y):
        self.figur = None
        self.x = x
        self.y = y
        self.matrixpos = None
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def set_Field_position(self, x, y):
        """sets the postion of the Field"""
        self.x = x
        self.y = y

    def get_Field_position(self):
        """gets the postion of the Field"""
        return self.x , self.y
