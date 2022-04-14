import pygame
import numpy as np


class Figur:
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

    def beat_figure(self, figure):
        if figure.player.color != self.player.color:
            if type(figure) == King:
                print(self.player.color + " wins")
                return True
            else:
                return True
        else:
            return False

    def is_field_allowed(self, infield):
        """checks if the figure is allowed to move to that field"""
        figure  = self.spiel.matrix[infield[0]][infield[1]].figur
        if self.spiel.matrix[infield[0]][infield[1]].figur!= None:

            return self.beat_figure(figure)
        else:
            return True

    def is_way_free(self, infield):
        x = infield[0] - self.field[0]
        y = infield[1] - self.field[1]
        a = 1
        b = 1

        if x < 0:
            a = -1
        if y < 0:
            b = -1

        if x == 0:
            for j in range(b, y, b):
                if self.spiel.matrix[self.field[0]][self.field[1] + j].figur != None:
                    return False

        elif y == 0:
            for i in range(a, x, a):
                if self.spiel.matrix[self.field[0] + i][self.field[1]].figur != None:
                    print(self.field[0] + i, self.field[0])
                    return False

        elif np.abs(x) == np.abs(y):
            for i in range(np.abs(x)):

                if self.spiel.matrix[self.field[0] + a*i][self.field[1] + b*i].figur != None:
                    return False
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
        x = np.abs(self.field[0] - infield[0])
        y = np.abs(self.field[1] - infield[1])

        if y == 0 and x > 0 or y > 0 and x == 0:

            return self.is_way_free(infield)
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
            return self.is_way_free(infield)
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
            return self.is_way_free(infield)
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
            return self.is_way_free(infield)
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
        if x == 2 and y == 1 or x == 1 and y == 2:
            return True
        else:
            return False
