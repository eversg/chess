import pygame
import numpy as np

class Figur():
    """single game figure with properties"""
    def __init__(self, image, spiel, player):
        self.player = player
        self.spiel = spiel
        self.x = 0
        self.y = 0
        self.field = None
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def set_Figur_position(self, x ,y):
        """sets Figur position"""
        self.x = x
        self.y = y

    def get_Figur_position(self):
        """gets Figur position"""
        return self.x, self.y

    def is_field_allowed(self, infield):
        """checks if the figure is allowed to move to that field"""
        if self.spiel.matrix[infield[0]][infield[1]].figur != None:
            print("hello")
            return False
        else:
            return True



class Bauer(Figur):

    def is_field_allowed(self, infield):
        d = super().is_field_allowed(infield)
        if not d:
            return False
        x = self.field[0] - infield[0]
        y = np.abs(self.field[1] - infield[1])
        if self.player.color == "black":
            if x == -1 and y == 0:
                return True
            else:
                return False
        elif self.player.color == "white":
            if x == 1 and y == 0:
                return True
            else:
                return False

class Turm(Figur):

    def is_field_allowed(self, infield):
        d = super().is_field_allowed(infield)
        if not d:
            return False
        print("hier")
        x = np.abs(self.field[0] - infield[0])
        y = np.abs(self.field[1] - infield[1])

        if y == 0 and x > 0 or y > 0 and x == 0:
            return True
        else:
            return False



class Springer(Figur):

    def is_field_allowed(self, infield):
        d = super().is_field_allowed(infield)
        if not d:
            return False
        x = np.abs(self.field[0] - infield[0])
        y = np.abs(self.field[1] - infield[1])

        if x == y and x > 0:
            return True
        else:
            return False

class King(Figur):

    def is_field_allowed(self, infield):
        d = super().is_field_allowed(infield)
        if not d:
            return False
        x = np.abs(self.field[0] - infield[0])
        y = np.abs(self.field[1] - infield[1])

        if x == 1 and y == 0 or y == 1 and x == 0 or y == 1 and  x == 1:
            return True
        else:
            return False


class Queen(Figur):

    def is_field_allowed(self, infield):
        d = super().is_field_allowed(infield)
        if not d:
            return False
        x = np.abs(self.field[0] - infield[0])
        y = np.abs(self.field[1] - infield[1])
        print(x)
        print(y)
        if x == y and  x > 0 or x > 0 and y == 0 or x == 0 and y > 0:
            return True
        else:
            return False

class Horse(Figur):

    def is_field_allowed(self, infield):
        d = super().is_field_allowed(infield)
        if not d:
            return False
        x = np.abs(self.field[0] - infield[0])
        y = np.abs(self.field[1] - infield[1])
        print(x)
        print(y)
        if x == 2 and  y == 1 or x == 1 and y == 2:
            return True
        else:
            return False