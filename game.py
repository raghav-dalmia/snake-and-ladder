import pygame
import sys
import random
import time
from math import floor

#colors
blue = (100,149,237)

player_turn = "one"

dice = {
    "normal" : {
        1 : "./images/dice/normal/1.png",
        2 : "./images/dice/normal/2.png",
        3 : "./images/dice/normal/3.png",
        4 : "./images/dice/normal/4.png",
        5 : "./images/dice/normal/5.png",
        6 : "./images/dice/normal/6.png",
    },
    "expanded" : {
        1 : "./images/dice/expanded/1.png",
        2 : "./images/dice/expanded/2.png",
        3 : "./images/dice/expanded/3.png",
        4 : "./images/dice/expanded/4.png",
        5 : "./images/dice/expanded/5.png",
        6 : "./images/dice/expanded/6.png",
    }
}

board_pos = []

def get_pos(player_pos,player):
    player_pos = player_pos -1
    x_pos = int(player_pos%10)
    y_pos = int(floor(player_pos/10))
    pos = board_pos[y_pos][x_pos]
    if player == 1:
        pos[0] = pos[0] + 3
        pos[1] = pos[1] + 3
    else:
        pos[0] = pos[0] + 6
        pos[1] = pos[1] + 6
    return pos

def start():
    x,y = -56.4,564
    for i in range (0,10):
        y = y - 56.4
        temp = []
        for j in range (0,10):
            if(i%2 == 0):
                x = x + 56.4
            else:
                x = x - 56.4
            temp.append([x,y])
        board_pos.append(temp)
    for i in board_pos:
        print(i)
    pygame.init()
    pygame.font.init()
    game_display = pygame.display.set_mode((850,564))
    pygame.display.set_caption("sanke and lader")
    clock = pygame.time.Clock()
    crashed = False
    board = pygame.image.load("./images/board.jpg")
    number = pygame.image.load("./images/dice/normal/1.png")
    play1 = pygame.image.load("./images/pices/yellow.png")
    play2 = pygame.image.load("./images/pices/green.png")
    board_rect = board.get_rect()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    
    steps = random.randrange(1,4)
    start = False
    player = 1
    pos = {
        1 : 0,
        2 : 0
    }
    player_pos ={
        1 : [624,500],
        2 : [574,500]
    }
    
    text1 = "press any key to start"
    text2 = ""
    text3 = ""
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN:
                if not start :
                    start = True
                    text1 = "press spacebar to throw dice"
                    text3 = "player " + str(player) + "\'s turn"
                else:
                    num = random.randrange(1,6)
                    number = pygame.image.load(dice["normal"][num])
                    text2 = "number is : " + str(num)
                    player = 3 - player
                    text3 = "player " + str(player) + "\'s turn"
                    if((num == 1 or num ==6) and pos[player] == 0):
                        pos[player] = 1
                    else:
                        pos[player] = pos[player] + num
                    player_pos[player] = get_pos(pos[player],player)
                    print("player " + str(player))
                    print("pos " + str(pos[player]))
                    print("piece pos " + str(player_pos[player]))

        game_display.fill(blue)
        game_display.blit(board,board_rect)

        text1surface = myfont.render(text1, False, (0, 0, 0))
        game_display.blit(text1surface,(575,0))

        text2surface = myfont.render(text2, False, (0, 0, 0))
        game_display.blit(text2surface,(575,230))

        text3surface = myfont.render(text3, False, (0, 0, 0))
        game_display.blit(text3surface,(575,260))

        game_display.blit(number,[625,70])

        game_display.blit(play1,player_pos[1])

        game_display.blit(play2,player_pos[2])

        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
    quit()
    sys.exit(0)
    
    
                