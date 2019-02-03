import pygame
import sys
from TicTacToe import TicTacToe
from MenuView import MenuView
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
MENU_COLOR = (234, 255, 34)

class MainController:
    def __init__(self,GRID_SIZE,players):
        self.players = players
        self.View = MenuView(3,players)

    
    def run(self):
        buttons1,buttons2,PlayButton = self.View.draw_Menu(self.players)
        
        flag = 0
        p1 = None
        p2 = None

        while(flag==0):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit()
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if(p1!=None and p2!=None):
                        if(PlayButton.isClicked(event)==1):
                            flag = 1
                    for i,b in enumerate(buttons1):
                        if(b.isClicked(event)>0):
                            p1 = self.players[i]
                            for bb in buttons1:
                                bb.UnToggle()
                            b.Toggle()
                    for i,b in enumerate(buttons2):
                        if(b.isClicked(event)>0):
                            p2 = self.players[i]
                            for bb in buttons2:
                                bb.UnToggle()
                            b.Toggle()

        print("!!!")


        A_TicTacToe = TicTacToe(3,3,p1,p2)
        A_TicTacToe.run()

        pygame.time.wait(30000)