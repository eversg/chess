from Figure import Bauer, Queen, King, Springer, Horse, Turm
import pygame
import os

class Player():
    """single player"""
    def __init__(self, spiel, color):
        self.spiel = spiel
        self.color = color
        imageurl = "images/" + self.color + "/" + self.color
        self.figures = [[Turm(pygame.image.load(imageurl + "tower.png"), spiel, self), Horse(pygame.image.load(imageurl + "horse.png"), spiel, self),
                         Springer(pygame.image.load(imageurl + "jumper.png"), spiel, self), King(pygame.image.load(imageurl + "king.png"), spiel, self),
                         Queen(pygame.image.load(imageurl + "queen.png"), spiel, self), Springer(pygame.image.load(imageurl + "jumper.png"), spiel, self),
                         Horse(pygame.image.load(imageurl + "horse.png"), spiel, self), Turm(pygame.image.load(imageurl + "tower.png"), spiel,self)],[]]
        for x in range(8):
            self.figures[1].append(Bauer(pygame.image.load(imageurl + "bauer.png"), spiel, self))

