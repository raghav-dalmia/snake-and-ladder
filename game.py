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

        if(i%2==0):
            x = x + 56.4
        else:
            x = x - 56.4
        
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
    play1 = pygame.image.load("./images/pices/black.png")
    play2 = pygame.image.load("./images/pices/yellow.png")
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

                    #opponent attack
                    if(pos[player] == pos[3-player]):
                        pos[3-player] = 0;

                    #ladders
                    if(pos[player] == 2):
                        pos[player] = 38
                    if(pos[player] == 7):
                        pos[player] = 14
                    if(pos[player] == 8):
                        pos[player] = 31
                    if(pos[player] == 15):
                        pos[player] = 26
                    if(pos[player] == 21):
                        pos[player] = 42
                    if(pos[player] == 28):
                        pos[player] = 84
                    if(pos[player] == 36):
                        pos[player] = 44
                    if(pos[player] == 51):
                        pos[player] = 67
                    if(pos[player] == 71):
                        pos[player] = 91
                    if(pos[player] == 78):
                        pos[player] = 98
                    if(pos[player] == 87):
                        pos[player] = 94
                    
                    #snakes
                    if(pos[player] == 16):
                        pos[player] = 6
                    if(pos[player] == 46):
                        pos[player] = 25
                    if(pos[player] == 49):
                        pos[player] = 11
                    if(pos[player] == 62):
                        pos[player] = 19
                    if(pos[player] == 64):
                        pos[player] = 60
                    if(pos[player] == 74):
                        pos[player] = 53
                    if(pos[player] == 89):
                        pos[player] = 68
                    if(pos[player] == 92):
                        pos[player] = 88
                    if(pos[player] == 95):
                        pos[player] = 75
                    if(pos[player] == 99):
                        pos[player] = 80


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


    
                
