######################################################
###############-  JOGO DA VELHA  -####################
###############- Marlyson Xavier -####################
######################################################

import pygame
import time
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
display_width = 700
display_height = 730

animation_increment = 10
clock_tick_rate = 60
size = (display_width, display_height)
gameDisplay = pygame.display.set_mode((size),32)

Jogador_X = 1
Jogador_O = 2

Jogador = 1

black = (0,0,0)
white = (223,223,223)
red = (200,0,0)
blue = (0,0,255)
bright_red = (255,0,0)
bright_white = (255,255,255)

Vazio1 = " "
Vazio2 = " "
Vazio3 = " "
Vazio4 = " "
Vazio5 = " "
Vazio6 = " "
Vazio7 = " "
Vazio8 = " "
Vazio9 = " "

pygame.display.set_caption('Jogo da Velha V1.1 - By Marlyson Xavier')
clock = pygame.time.Clock()

X1 = ' '
X2 = ' '
X3 = ' '
X4 = ' '
X5 = ' '
X6 = ' '
X7 = ' '
X8 = ' '
X9 = ' '
O1 = ' '
O2 = ' '
O3 = ' '
O4 = ' '
O5 = ' '
O6 = ' '
O7 = ' '
O8 = ' '
O9 = ' '

Jogadas = 0

X = "X"
O = "O"

bot1 = 0
bot2 = 0
bot3 = 0
bot4 = 0
bot5 = 0
bot6 = 0
bot7 = 0
bot8 = 0
bot9 = 0

def limpar():
	os.system('cls') or None

def Botao_Fechar(msg,t,x,y,w,h,ic,ac,acao=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and acao != None:
            if acao == "EXIT":
                Agradecimento()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.Font('freesansbold.ttf', t)
    TextSurf, TextRect = Texto_Preto(msg, smallText)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(TextSurf, TextRect)

def Botao_C(msg,t,x,y,w,h,ic,ac,acao=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and acao != None:
            if acao == "SIM":
                main()
            if acao == "NÃO":
                Agradecimento()
            if acao == "EXIT":
                Agradecimento()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.Font('freesansbold.ttf', t)
    TextSurf, TextRect = Texto_Preto(msg, smallText)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(TextSurf, TextRect)

def botao_X1(t,x,y,w,h,ic,ac,acao=None):
    global Vazio1
    global Jogadas
    global Jogador
    global X1
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio1, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot1
            if acao == "1" and bot1 == 0:
                bot1 = bot1 + 1
                print(bot1)
                print("Botão X - 1")
                X1 = 'X'
                Jogador = 2
                Vazio1 = X
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_O()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio1, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_X2(t,x,y,w,h,ic,ac,acao=None):
    global Vazio2
    global Jogadas
    global Jogador
    global X2
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio2, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot2
            if acao == "2" and bot2 == 0:
                bot2 = bot2 + 1
                print(bot2)
                print("Botão X - 2")
                X2 = 'X'
                Jogador = 2
                Vazio2 = X
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_O()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio2, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_X3(t,x,y,w,h,ic,ac,acao=None):
    global Vazio3
    global Jogadas
    global Jogador
    global X3
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio3, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot3
            if acao == "3" and bot3 == 0:
                bot3 = bot3 + 1
                print(bot3)
                print("Botão X - 3")
                X3 = 'X'
                Jogador = 2
                Vazio3 = X
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_O()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio3, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_X4(t,x,y,w,h,ic,ac,acao=None):
    global Vazio4
    global Jogadas
    global Jogador
    global X4
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio4, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot4
            if acao == "4" and bot4 == 0:
                bot4 = bot4 + 1
                print(bot4)
                print("Botão X - 4")
                X4 = 'X'
                Jogador = 2
                Vazio4 = X
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_O()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio4, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_X5(t,x,y,w,h,ic,ac,acao=None):
    global Vazio5
    global Jogadas
    global Jogador
    global X5
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio5, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot5
            if acao == "5" and bot5 == 0:
                bot5 = bot5 + 1
                print(bot5)
                print("Botão X - 5")
                X5 = 'X'
                Jogador = 2
                Vazio5 = X
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_O()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio5, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_X6(t,x,y,w,h,ic,ac,acao=None):
    global Vazio6
    global Jogadas
    global Jogador
    global X6
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio6, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot6
            if acao == "6" and bot6 == 0:
                bot6 = bot6 + 1
                print(bot6)
                print("Botão X - 6")
                X6 = 'X'
                Jogador = 2
                Vazio6 = X
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_O()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio6, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_X7(t,x,y,w,h,ic,ac,acao=None):
    global Vazio7
    global Jogadas
    global Jogador
    global X7
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio7, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot7
            if acao == "7" and bot7 == 0:
                bot7 = bot7 + 1
                print(bot7)
                print("Botão X - 7")
                X7 = 'X'
                Jogador = 2
                Vazio7 = X
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_O()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio7, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_X8(t,x,y,w,h,ic,ac,acao=None):
    global Vazio8
    global Jogadas
    global Jogador
    global X8
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio8, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot8
            if acao == "8" and bot8 == 0:
                bot8 = bot8 + 1
                print(bot8)
                print("Botão X - 8")
                X8 = 'X'
                Jogador = 2
                Vazio8 = X
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_O()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio8, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_X9(t,x,y,w,h,ic,ac,acao=None):
    global Vazio9
    global Jogadas
    global Jogador
    global X9
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio9, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot9
            if acao == "9" and bot9 == 0:
                bot9 = bot9 + 1
                print(bot9)
                print("Botão X - 9")
                X9 = 'X'
                Jogador =2
                Vazio9 = X
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_O()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio9, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_O1(t,x,y,w,h,ic,ac,acao=None):
    global Vazio1
    global Jogadas
    global Jogador
    global O1
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio1, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot1
            if acao == "1" and bot1 == 0:
                bot1 = bot1 + 2
                print(bot1)
                print("Botão O - 1")
                O1 = 'O'
                Jogador = 1
                Vazio1 = O
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_X()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio1, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_O2(t,x,y,w,h,ic,ac,acao=None):
    global Vazio2
    global Jogadas
    global Jogador
    global O2
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio2, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot2
            if acao == "2" and bot2 == 0:
                bot2 = bot2 + 2
                print(bot2)
                print("Botão O - 2")
                O2 = 'O'
                Jogador = 1
                Vazio2 = O
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_X()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio2, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_O3(t,x,y,w,h,ic,ac,acao=None):
    global Vazio3
    global Jogadas
    global Jogador
    global O3
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio3, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot3
            if acao == "3" and bot3 == 0:
                bot3 = bot3 + 2
                print(bot3)
                print("Botão O - 3")
                O3 = 'O'
                Jogador = 1
                Vazio3 = O
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_X()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio3, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_O4(t,x,y,w,h,ic,ac,acao=None):
    global Vazio4
    global Jogadas
    global Jogador
    global O4
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio4, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot4
            if acao == "4" and bot4 == 0:
                bot4 = bot4 + 2
                print(bot4)
                print("Botão O - 4")
                O4 = 'O'
                Jogador = 1
                Vazio4 = O
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_X()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio4, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_O5(t,x,y,w,h,ic,ac,acao=None):
    global Vazio5
    global Jogadas
    global Jogador
    global O5
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio5, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot5
            if acao == "5" and bot5 == 0:
                bot5 = bot5 + 2
                print(bot5)
                print("Botão O - 5")
                O5 = 'O'
                Jogador = 1
                Vazio5 = O
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_X()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio5, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_O6(t,x,y,w,h,ic,ac,acao=None):
    global Vazio6
    global Jogadas
    global Jogador
    global O6
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio6, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot6
            if acao == "6" and bot6 == 0:
                bot6 = bot6 + 2
                print(bot6)
                print("Botão O - 6")
                O6 = 'O'
                Jogador = 1
                Vazio6 = O
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_X()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio6, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_O7(t,x,y,w,h,ic,ac,acao=None):
    global Vazio7
    global Jogadas
    global Jogador
    global O7
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio7, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot7
            if acao == "7" and bot7 == 0:
                bot7 = bot7 + 2
                print(bot7)
                print("Botão O - 7")
                O7 = 'O'
                Jogador = 1
                Vazio7 = O
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_X()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio7, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_O8(t,x,y,w,h,ic,ac,acao=None):
    global Vazio8
    global Jogadas
    global Jogador
    global O8
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio8, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot8
            if acao == "8" and bot8 == 0:
                bot8 = bot8 + 2
                print(bot8)
                print("Botão O - 8")
                O8 = 'O'
                Jogador = 1
                Vazio8 = O
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_X()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio8, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def botao_O9(t,x,y,w,h,ic,ac,acao=None):
    global Vazio9
    global Jogadas
    global Jogador
    global O9
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio9, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1 and acao != None:
            global bot9
            if acao == "9" and bot9 == 0:
                bot9 = bot9 + 2
                print(bot9)
                print("Botão O - 0")
                O9 = 'O'
                Jogador = 1
                Vazio9 = O
                Jogadas = Jogadas + 1
                time.sleep(0.5)
                velha_X()
            else:
                print("Opção já utilizada!!!")
                time.sleep(1)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf', t)
        TextSurf, TextRect = Texto_Preto(Vazio9, smallText)
        TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(TextSurf, TextRect)

def velha_X():
    global X1
    global X2
    global X3
    global X4
    global X5
    global X6
    global X7
    global X8
    global X9
    global Jogador_X
    global Jogadas
    Jogar = True
    while Jogar:
        for event in pygame.event.get():
            global Jogador
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif Jogador == 1:
                if X1 == X2 == X3 == 'X':
                    print("Ganhou X - 1 2 3 !!!")
                    Jogador = 1
                    ganhou_X()
                if X4 == X5 == X6 == 'X':
                    print("Ganhou X - 4 5 6 !!!")
                    Jogador = 1
                    ganhou_X()
                if X7 == X8 == X9 == 'X':
                    print("Ganhou X - 7 8 9 !!!")
                    Jogador = 1
                    ganhou_X()
                if X1 == X4 == X7 == 'X':
                    print("Ganhou X - 1 4 7 !!!")
                    Jogador = 1
                    ganhou_X()
                if X2 == X5 == X8 == 'X':
                    print("Ganhou X - 2 5 8 !!!")
                    Jogador = 1
                    ganhou_X()
                if X3 == X6 == X9 == 'X':
                    print("Ganhou X - 3 6 9 !!!")
                    Jogador = 1
                    ganhou_X()
                if X1 == X5 == X9 == 'X':
                    print("Ganhou X - 1 5 9!!!")
                    Jogador = 1
                    ganhou_X()
                if X7 == X5 == X3 == 'X':
                    print("Ganhou X - 7 5 3 !!!")
                    Jogador = 1
                    ganhou_X()

                if Jogadas == 9:
                    if X1 == X2 == X3 == 'X':
                        print("Ganhou X - 1 2 3 !!!")
                        Jogador = 1
                        ganhou_X()
                    if X4 == X5 == X6 == 'X':
                        print("Ganhou X - 4 5 6 !!!")
                        Jogador = 1
                        ganhou_X()
                    if X7 == X8 == X9 == 'X':
                        print("Ganhou X - 7 8 9 !!!")
                        Jogador = 1
                        ganhou_X()
                    if X1 == X4 == X7 == 'X':
                        print("Ganhou X - 1 4 7 !!!")
                        Jogador = 1
                        ganhou_X()
                    if X2 == X5 == X8 == 'X':
                        print("Ganhou X - 2 5 8 !!!")
                        Jogador = 1
                        ganhou_X()
                    if X3 == X6 == X9 == 'X':
                        print("Ganhou X - 3 6 9 !!!")
                        Jogador = 1
                        ganhou_X()
                    if X1 == X5 == X9 == 'X':
                        print("Ganhou X - 1 5 9!!!")
                        Jogador = 1
                        ganhou_X()
                    if X7 == X5 == X3 == 'X':
                        print("Ganhou X - 7 5 3 !!!")
                        Jogador = 1
                        ganhou_X()
                    if O1 == O2 == O3 == 'O':
                        print("Ganhou O - 1 2 3 !!!")
                        Jogador = 1
                        ganhou_O()
                    if O4 == O5 == O6 == 'O':
                        print("Ganhou O - 4 5 6 !!!")
                        Jogador = 1
                        ganhou_O()
                    if O7 == O8 == O9 == 'O':
                        print("Ganhou O - 7 8 9 !!!")
                        Jogador = 1
                        ganhou_O()
                    if O1 == O4 == O7 == 'O':
                        print("Ganhou O - 1 4 7 !!!")
                        Jogador = 1
                        ganhou_O()
                    if O2 == O5 == O8 == 'O':
                        print("Ganhou O - 2 5 8 !!!")
                        Jogador = 1
                        ganhou_O()
                    if O3 == O6 == O9 == 'O':
                        print("Ganhou O - 3 6 9 !!!")
                        Jogador = 1
                        ganhou_O()
                    if O1 == O5 == O9 == 'O':
                        print("Ganhou O - 1 5 9!!!")
                        Jogador = 1
                        ganhou_O()
                    if O7 == O5 == O3 == 'O':
                        print("Ganhou O - 7 5 3 !!!")
                        Jogador = 1
                        ganhou_O()
                    else:
                        velha()

                else:
                    gameDisplay.fill(black)
                    largeText = pygame.font.Font('freesansbold.ttf', 15)
                    TextSurf, TextRect = Texto_Vermelho("JOGO DA VELHA - BY MARLYSON XAVIER - Jogador 1", largeText)
                    TextRect.center = ((display_width / 2), (15))
                    gameDisplay.blit(TextSurf, TextRect)
                    Botao_Fechar("X", 15, 670, 5, 20, 20, red, bright_red, "EXIT")
                    botao_X1(180, 10, 30, 220, 220, bright_white, white, "1")
                    botao_X2(180, 240, 30, 220, 220, bright_white, white, "2")
                    botao_X3(180, 470, 30, 220, 220, bright_white, white, "3")
                    botao_X4(180, 10, 260, 220, 220, bright_white, white, "4")
                    botao_X5(180, 240, 260, 220, 220, bright_white, white, "5")
                    botao_X6(180, 470, 260, 220, 220, bright_white, white, "6")
                    botao_X7(180, 10, 490, 220, 220, bright_white, white, "7")
                    botao_X8(180, 240, 490, 220, 220, bright_white, white, "8")
                    botao_X9(180, 470, 490, 220, 220, bright_white, white, "9")
                    pygame.display.update()
                    clock.tick(clock_tick_rate)

def velha_O():
    global Jogador_O
    global Jogadas
    global O1
    global O2
    global O3
    global O4
    global O5
    global O6
    global O7
    global O8
    global O9

    Jogar = True
    while Jogar:
        for event in pygame.event.get():
            global Jogador
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif Jogador == 2:
                if O1 == O2 == O3 == 'O':
                    print("Ganhou O - 1 2 3 !!!")
                    Jogador = 1
                    ganhou_O()
                if O4 == O5 == O6 == 'O':
                    print("Ganhou O - 4 5 6 !!!")
                    Jogador = 1
                    ganhou_O()
                if O7 == O8 == O9 == 'O':
                    print("Ganhou O - 7 8 9 !!!")
                    Jogador = 1
                    ganhou_O()
                if O1 == O4 == O7 == 'O':
                    print("Ganhou O - 1 4 7 !!!")
                    Jogador = 1
                    ganhou_O()
                if O2 == O5 == O8 == 'O':
                    print("Ganhou O - 2 5 8 !!!")
                    Jogador = 1
                    ganhou_O()
                if O3 == O6 == O9 == 'O':
                    print("Ganhou O - 3 6 9 !!!")
                    Jogador = 1
                    ganhou_O()
                if O1 == O5 == O9 == 'O':
                    print("Ganhou O - 1 5 9!!!")
                    Jogador = 1
                    ganhou_O()
                if O7 == O5 == O3 == 'O':
                    print("Ganhou O - 7 5 3 !!!")
                    Jogador = 1
                    ganhou_O()

                if Jogadas == 9:
                    if X1 == X2 == X3 == 'X':
                        print("Ganhou X - 1 2 3 !!!")
                        Jogador = 1
                        ganhou_X()
                    if X4 == X5 == X6 == 'X':
                        print("Ganhou X - 4 5 6 !!!")
                        Jogador = 1
                        ganhou_X()
                    if X7 == X8 == X9 == 'X':
                        print("Ganhou X - 7 8 9 !!!")
                        Jogador = 1
                        ganhou_X()
                    if X1 == X4 == X7 == 'X':
                        print("Ganhou X - 1 4 7 !!!")
                        Jogador = 1
                        ganhou_X()
                    if X2 == X5 == X8 == 'X':
                        print("Ganhou X - 2 5 8 !!!")
                        Jogador = 1
                        ganhou_X()
                    if X3 == X6 == X9 == 'X':
                        print("Ganhou X - 3 6 9 !!!")
                        Jogador = 1
                        ganhou_X()
                    if X1 == X5 == X9 == 'X':
                        print("Ganhou X - 1 5 9!!!")
                        Jogador = 1
                        ganhou_X()
                    if X7 == X5 == X3 == 'X':
                        print("Ganhou X - 7 5 3 !!!")
                        Jogador = 1
                        ganhou_X()
                    if O1 == O2 == O3 == 'O':
                        print("Ganhou O - 1 2 3 !!!")
                        Jogador = 1
                        ganhou_O()
                    if O4 == O5 == O6 == 'O':
                        print("Ganhou O - 4 5 6 !!!")
                        Jogador = 1
                        ganhou_O()
                    if O7 == O8 == O9 == 'O':
                        print("Ganhou O - 7 8 9 !!!")
                        Jogador = 1
                        ganhou_O()
                    if O1 == O4 == O7 == 'O':
                        print("Ganhou O - 1 4 7 !!!")
                        Jogador = 1
                        ganhou_O()
                    if O2 == O5 == O8 == 'O':
                        print("Ganhou O - 2 5 8 !!!")
                        Jogador = 1
                        ganhou_O()
                    if O3 == O6 == O9 == 'O':
                        print("Ganhou O - 3 6 9 !!!")
                        Jogador = 1
                        ganhou_O()
                    if O1 == O5 == O9 == 'O':
                        print("Ganhou O - 1 5 9!!!")
                        Jogador = 1
                        ganhou_O()
                    if O7 == O5 == O3 == 'O':
                        print("Ganhou O - 7 5 3 !!!")
                        Jogador = 1
                        ganhou_O()
                    else:
                        velha()

                else:
                    gameDisplay.fill(black)
                    largeText = pygame.font.Font('freesansbold.ttf', 15)
                    TextSurf, TextRect = Texto_Vermelho("JOGO DA VELHA - BY MARLYSON XAVIER - Jogador 2", largeText)
                    TextRect.center = ((display_width / 2), (15))
                    gameDisplay.blit(TextSurf, TextRect)
                    Botao_Fechar("X", 15, 670, 5, 20, 20, red, bright_red, "EXIT")
                    botao_O1(180, 10, 30, 220, 220, bright_white, white, "1")
                    botao_O2(180, 240, 30, 220, 220, bright_white, white, "2")
                    botao_O3(180, 470, 30, 220, 220, bright_white, white, "3")
                    botao_O4(180, 10, 260, 220, 220, bright_white, white, "4")
                    botao_O5(180, 240, 260, 220, 220, bright_white, white, "5")
                    botao_O6(180, 470, 260, 220, 220, bright_white, white, "6")
                    botao_O7(180, 10, 490, 220, 220, bright_white, white, "7")
                    botao_O8(180, 240, 490, 220, 220, bright_white, white, "8")
                    botao_O9(180, 470, 490, 220, 220, bright_white, white, "9")
                    pygame.display.update()
                    clock.tick(clock_tick_rate)

def ganhou_X():
    ganhou = True
    while ganhou:
        for event in pygame.event.get():
            global Jogador
            gameDisplay.fill(black)
            largeText = pygame.font.Font('freesansbold.ttf', 15)
            TextSurf, TextRect = Texto_Vermelho("JOGO DA VELHA - BY MARLYSON XAVIER", largeText)
            TextRect.center = ((display_width / 2), (15))
            gameDisplay.blit(TextSurf, TextRect)
            Botao_Fechar("X", 15, 670, 5, 20, 20, red, bright_red, "EXIT")
            Botao_C("Player 'X' Ganhou!!!",50, 10, 30, 680, 220, bright_white, bright_white, '')
            Botao_C('CONTINUAR?',50, 10, 260, 680, 220, bright_white, bright_white, '')
            Botao_C('SIM',80, 10, 490, 220, 220, bright_white, bright_white, "SIM")
            Botao_C('',180, 240, 490, 220, 220, bright_white, bright_white, '')
            Botao_C('NÃO',80, 470, 490, 220, 220, bright_white, bright_white, "NÃO")
            pygame.display.update()
            clock.tick(clock_tick_rate)

def ganhou_O():
    Jogar = True
    while Jogar:
        for event in pygame.event.get():
            global Jogador
            gameDisplay.fill(black)
            largeText = pygame.font.Font('freesansbold.ttf', 15)
            TextSurf, TextRect = Texto_Vermelho("JOGO DA VELHA - BY MARLYSON XAVIER", largeText)
            TextRect.center = ((display_width / 2), (15))
            gameDisplay.blit(TextSurf, TextRect)
            Botao_Fechar("X", 15, 670, 5, 20, 20, red, bright_red, "EXIT")
            Botao_C("Player 'O' Ganhou!!! ",50, 10, 30, 680, 220, bright_white, bright_white, '')
            Botao_C('CONTINUAR?',50, 10, 260, 680, 220, bright_white, bright_white, '')
            Botao_C('SIM',80, 10, 490, 220, 220, bright_white, bright_white, "SIM")
            Botao_C('',180, 240, 490, 220, 220, bright_white, bright_white, '')
            Botao_C('NÃO',80, 470, 490, 220, 220, bright_white, bright_white, "NÃO")
            pygame.display.update()
            clock.tick(clock_tick_rate)

def velha():
    ganhou = True
    while ganhou:
        for event in pygame.event.get():
            global Jogador
            gameDisplay.fill(black)
            largeText = pygame.font.Font('freesansbold.ttf', 15)
            TextSurf, TextRect = Texto_Vermelho("JOGO DA VELHA - BY MARLYSON XAVIER", largeText)
            TextRect.center = ((display_width / 2), (15))
            gameDisplay.blit(TextSurf, TextRect)
            Botao_Fechar("X", 15, 670, 5, 20, 20, red, bright_red, "EXIT")
            Botao_C("V E L H A!!!",50, 10, 30, 680, 220, bright_white, bright_white, '')
            Botao_C('CONTINUAR?',50, 10, 260, 680, 220, bright_white, bright_white, '')
            Botao_C('SIM',80, 10, 490, 220, 220, bright_white, bright_white, "SIM")
            Botao_C('',180, 240, 490, 220, 220, bright_white, bright_white, '')
            Botao_C('NÃO',80, 470, 490, 220, 220, bright_white, bright_white, "NÃO")
            pygame.display.update()
            clock.tick(clock_tick_rate)

def Texto_Vermelho(text,font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def Texto_Preto(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def Texto_Branco(text,font):
    textSurface = font.render(text, True, bright_white)
    return textSurface, textSurface.get_rect()

def Texto_Azul(text,font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def Linha_01(linhax, linhay, linhaw, linhah, color):
    pygame.draw.rect(gameDisplay, color, [linhax, linhay, linhaw, linhah])

def Agradecimento():

    linha = [730,790,850,910,970,1030,1090,1120]

    linhaSpeed = 1
    historia = True
    while historia:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                time.sleep(0.5)
                pygame.quit()
                quit()
        gameDisplay.fill(black)

        Linha_01(0, linha[0], 700, 100, black)
        linha[0] -= linhaSpeed
        smallText = pygame.font.Font('freesansbold.ttf',25)
        TextSurf, TextRect = Texto_Branco("J O G O   D A   V E L H A  #", smallText)
        TextRect.center = ((0 + (700 / 2)), (linha[0] + (30 / 2)))
        gameDisplay.blit(TextSurf, TextRect)

        Linha_01(0, linha[1], 700, 60, black)
        linha[1] -= linhaSpeed
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = Texto_Branco("O B R I G A D O   P O R   J O G A R", smallText)
        TextRect.center = ((0 + (700 / 2)), (linha[1] + (30 / 2)))
        gameDisplay.blit(TextSurf, TextRect)

        Linha_01(0, linha[2], 700, 60, black)
        linha[2] -= linhaSpeed
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = Texto_Branco("D E S E N V O L V I D O    P O R . . .", smallText)
        TextRect.center = ((0 + (700 / 2)), (linha[2] + (30 / 2)))
        gameDisplay.blit(TextSurf, TextRect)

        Linha_01(0, linha[3], 700, 60, black)
        linha[3] -= linhaSpeed
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = Texto_Branco("M A R L Y S O N   X A V I E R", smallText)
        TextRect.center = ((0 + (700 / 2)), (linha[3] + (30 / 2)))
        gameDisplay.blit(TextSurf, TextRect)

        Linha_01(0, linha[4], 700, 60, black)
        linha[4] -= linhaSpeed
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = Texto_Branco("E Q U I P E   J A M P A . C O M", smallText)
        TextRect.center = ((0 + (700 / 2)), (linha[4] + (30 / 2)))
        gameDisplay.blit(TextSurf, TextRect)

        Linha_01(0, linha[5], 700, 60, black)
        linha[5] -= linhaSpeed
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = Texto_Branco("P R O J E T O   E X E R C I C I O   A L I N E", smallText)
        TextRect.center = ((0 + (700 / 2)), (linha[5] + (30 / 2)))
        gameDisplay.blit(TextSurf, TextRect)

        Linha_01(0, linha[6], 700, 60, black)
        linha[6] -= linhaSpeed
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = Texto_Branco("Q   A U L A   0 4   -   M A T R I Z E S   -   T E D", smallText)
        TextRect.center = ((0 + (700 / 2)), (linha[6] + (30 / 2)))
        gameDisplay.blit(TextSurf, TextRect)

        linha_fim = ((linhaSpeed) - (linha[6]))
        if linha_fim == 50:
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(60)

def main():
    global Jogador_X
    global Jogadas
    global X1
    global X2
    global X3
    global X4
    global X5
    global X6
    global X7
    global X8
    global X9
    global O1
    global O2
    global O3
    global O4
    global O5
    global O6
    global O7
    global O8
    global O9
    global bot1
    global bot2
    global bot3
    global bot4
    global bot5
    global bot6
    global bot7
    global bot8
    global bot9
    global Vazio1
    global Vazio2
    global Vazio3
    global Vazio4
    global Vazio5
    global Vazio6
    global Vazio7
    global Vazio8
    global Vazio9
    global Jogador

    main = True
    while main:
        Jogador = 1
        Jogadas = 0
        X1 = ' '
        X2 = ' '
        X3 = ' '
        X4 = ' '
        X5 = ' '
        X6 = ' '
        X7 = ' '
        X8 = ' '
        X9 = ' '
        O1 = ' '
        O2 = ' '
        O3 = ' '
        O4 = ' '
        O5 = ' '
        O6 = ' '
        O7 = ' '
        O8 = ' '
        O9 = ' '
        bot1 = 0
        bot2 = 0
        bot3 = 0
        bot4 = 0
        bot5 = 0
        bot6 = 0
        bot7 = 0
        bot8 = 0
        bot9 = 0
        Vazio1 = " "
        Vazio2 = " "
        Vazio3 = " "
        Vazio4 = " "
        Vazio5 = " "
        Vazio6 = " "
        Vazio7 = " "
        Vazio8 = " "
        Vazio9 = " "
        if Jogadas >= 0:
            velha_X()

main()