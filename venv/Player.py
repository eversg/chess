from Figure import Bauer, Queen, King, Springer, Horse, Turm
import pygame

class Player():
    """single player"""
    def __init__(self, spiel, color):
        self.spiel = spiel
        self.color = color
        self.figures = [[Turm(pygame.image.load("bauer.png"), spiel), Horse(pygame.image.load("bauer.png"), spiel),
                         Springer(pygame.image.load("bauer.png"), spiel), King(pygame.image.load("bauer.png"), spiel),
                         King(pygame.image.load("bauer.png"), spiel), Springer(pygame.image.load("bauer.png"), spiel),
                         Horse(pygame.image.load("bauer.png"), spiel), Turm(pygame.image.load("bauer.png"), spiel)],
                        [Bauer(pygame.image.load("bauer.png"), spiel), Bauer(pygame.image.load("bauer.png"), spiel),
                         Bauer(pygame.image.load("bauer.png"), spiel), Bauer(pygame.image.load("bauer.png"), spiel),
                         Bauer(pygame.image.load("bauer.png"), spiel), Bauer(pygame.image.load("bauer.png"), spiel),
                         Bauer(pygame.image.load("bauer.png"), spiel), Bauer(pygame.image.load("bauer.png"), spiel)]]


