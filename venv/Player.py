from Figure import Bauer, Queen, King, Springer, Horse, Turm
import pygame

class Player():
    """single player"""
    def __init__(self, spiel, color):
        self.spiel = spiel
        self.color = color
        imageurl = self.color + "bauer.png"
        self.figures = [[Turm(pygame.image.load(imageurl), spiel, self), Horse(pygame.image.load(imageurl), spiel, self),
                         Springer(pygame.image.load(imageurl), spiel, self), King(pygame.image.load(imageurl), spiel,self),
                         King(pygame.image.load(imageurl), spiel, self), Springer(pygame.image.load(imageurl), spiel, self),
                         Horse(pygame.image.load(imageurl), spiel, self), Turm(pygame.image.load(imageurl), spiel,self)],
                        [Bauer(pygame.image.load(imageurl), spiel,self), Bauer(pygame.image.load(imageurl), spiel,self),
                         Bauer(pygame.image.load(imageurl), spiel, self), Bauer(pygame.image.load(imageurl), spiel,self),
                         Bauer(pygame.image.load(imageurl), spiel, self), Bauer(pygame.image.load(imageurl), spiel,self),
                         Bauer(pygame.image.load(imageurl), spiel, self), Bauer(pygame.image.load(imageurl), spiel,self)]]


