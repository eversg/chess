import pygame
from Figure import Figur, Bauer, Springer, Turm, King, Queen, Horse
from Player import Player
from Field import Field

class Spiel():
    """Game"""
    def __init__(self):
        self.matrix = [[],[],[],[],[],[],[],[]]      #Gamefield
        self.width, self.height = 800, 700           #resolution
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.players = [Player(self,"black"), Player(self, "white")]
        """       game images       """
        self.bg=  pygame.image.load("backround.png")
        self.gray = pygame.image.load("chessgray.png")
        self.white = pygame.image.load("chesswhite#.png")

        self.currentFigur = None                    #safes an object of a figure that is getting moved by the mouse
        self.pressed = False                        #bool to check if the mouse is currently pressed or not
        self.infield = [0, 0]                       #safes the current white or gray spot of the mouse position
        self.init_gamefield()

    def init_gamefield(self):
        """ sets the gamefield construction,
        splitting up the field in gray and white spots
        and places the figures on the field
        """

        i = -1
        for h in range(8):
            if i == -1 or i == 0:
                color = self.white
                i = 1
            else:
                color = self.gray
                i = 0
            for w in range(8):
                self.matrix[h].append(Field(color,w*color.get_width(),h*color.get_height()))
                self.matrix[h][w].matrixpos = [h, w]
                if i == -1 or i == 0:
                    color = self.white
                    i = 1
                else:
                    color = self.gray
                    i = 0
        """  placing the game figures on the field """
        for w in range(8):
            for j in range(2):
                for i in range(2):
                    self.matrix[i+(7-2*i)*j][w].figur = self.players[j].figures[i][w]
                    self.matrix[i+(7-2*i)*j][w].figur.set_Figur_position(self.matrix[i+(7-2*i)*j][w].x + 17, self.matrix[i+(7-2*i)*j][w].y + 10)


        self.gameloop()

    def gameloop(self):
        """"  gameloop  """
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.bg,(0,0))

            for h in range(8):
                for w in range(8):
                    fieldx, fieldy = self.matrix[h][w].get_Field_position()
                    self.screen.blit(self.matrix[h][w].image, (fieldx, fieldy))                                         #rendering the gamefield
                    if self.currentFigur != None:                                                                       #checks if the mouse moves a game figure
                        currentx, currenty = self.currentFigur.get_Figur_position()
                        if fieldx + self.matrix[h][w].width > currentx > fieldx:                                        #checks if the moving figure is in a white or black spot

                            if fieldy + self.matrix[h][w].height > currenty > fieldy:
                                self.infield = [h, w]                                                                   # safes in which white or black spot the current moving figure is

                    if self.matrix[h][w].figur!= None:
                        """draws the figures on the gamefield and checks if the mouse clicks on a figure"""
                        self.is_taken(self.matrix[h][w])

                        if self.matrix[h][w].figur != None:
                            figurx, figury = self.matrix[h][w].figur.get_Figur_position()
                            self.screen.blit(self.matrix[h][w].figur.image, (figurx, figury))

                    if self.currentFigur != None:
                        """draws the current moving figure on the field"""
                        currentx, currenty = self.currentFigur.get_Figur_position()
                        self.screen.blit(self.currentFigur.image,(currentx, currenty))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
            self.move()

    def is_taken(self, field):
        """checks if the mouse is on a figur and if the mouse got pressed"""
        if pygame.mouse.get_pressed()[0] and (self.pressed == False):

            mouse_posi = pygame.mouse.get_pos()
            x, y = field.figur.get_Figur_position()
            """ checks if the mouse on a figur """
            if (x <= mouse_posi[0] <= x + field.figur.width
                and y <= mouse_posi[1] <= y + field.figur.height):

                self.currentFigur = field.figur
                self.currentFigur.field = field.matrixpos
                field.figur = None
                self.pressed = True

    def move(self):
        """when the mouse is still pressed it moves the current moving figure on the new mouse position
        else it places the figure into the nearest gray or white spot"""
        if pygame.mouse.get_pressed()[0]:
            if self.pressed:
                mouse_posi = pygame.mouse.get_pos()
                self.currentFigur.set_Figur_position (mouse_posi[0], mouse_posi[1])

        else:

            if self.pressed:
                if self.currentFigur.is_field_allowed(self.infield):
                    a = self.matrix[self.infield[0]][self.infield[1]]
                    x, y= a.get_Field_position()
                    x += 15
                    y += 10
                    self.currentFigur.set_Figur_position(x, y)
                    a.figur = self.currentFigur

                else:
                    a = self.matrix[self.currentFigur.field[0]][self.currentFigur.field[1]]
                    x, y= a.get_Field_position()
                    x += 15
                    y += 10
                    self.currentFigur.set_Figur_position(x, y)
                    a.figur = self.currentFigur

            self.currentFigur = None
            self.pressed = False