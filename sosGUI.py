from sosAlgorithms import *
import pygame, sys
from pygame.locals import *

pygame.init()
maSurface = pygame.display.set_mode((1400,900))
pygame.display.set_caption('SOS')
inProgress = True
GREY = (128,128,128)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,51,153)
RED = (255,0,0)
maSurface.fill(GREY)
n = 6
l = 0
start = False
nb1 = 0
score1=[0,0]

def drawBoard(maSurface, n):

    pygame.draw.rect(maSurface, GREY, (100, 100, 700, 700), 0)
    pygame.draw.rect(maSurface, BLACK, (100,100,700,700), 3)

    taille = 700 // n

    for i in range(n):
        pygame.draw.line(maSurface,BLACK,(100 + i * taille,100),(100 + i * taille,800),3)
        pygame.draw.line(maSurface, BLACK, (100, 100 + i * taille), (800, 100 + i * taille), 3)

    police = pygame.font.Font("freesansbold.ttf", 250 // n)
    LettresS = police.render('S', True, BLACK)
    LettresO = police.render('O', True, BLACK)
    LettresM = police.render('|', True, BLACK)

    maSurface.blit(LettresS, (100 + taille * 1 / 6, 100 + taille * 1 / 3))
    maSurface.blit(LettresM, (97 + taille * 1 / 2, 100 + taille * 1 / 3))
    maSurface.blit(LettresO, (100 + taille * 3 / 5, 100 + taille * 1 / 3))

    for i in range(n):
         for j in range(n):
            maSurface.blit(LettresS, (100 + taille * 1 / 6 + i * taille, 100 + taille * 1 / 3 + j * taille))
            maSurface.blit(LettresM, (97 + taille * 1 / 2 + i * taille, 100 + taille * 1 / 3 + j * taille))
            maSurface.blit(LettresO, (100 + taille * 3 / 5 + i * taille, 100 + taille * 1 / 3 + j * taille))

    return taille

def  displayScore(maSurface,n,scores):

    font = pygame.font.Font(None, 75)
    pygame.draw.rect(maSurface, GREY, (1125, 193, 80, 80), 0)
    pygame.draw.rect(maSurface, GREY, (1160, 500, 80, 80), 0)
    pygame.draw.rect(maSurface, GREY, (374, 809, 80, 80), 0)
    text_p1 = font.render('Bleu : '+str(scores[0]),True,BLUE)
    text_p2 = font.render('Rouge : '+str(scores[1]),True,RED)

    maSurface.blit(text_p1, (977,200))
    maSurface.blit(text_p2, (970, 500))

def displayPlayer(mySurface,n,player,joueurs):
    font = pygame.font.Font(None, 40)

    text = font.render('Au tour du joueur '+str(joueurs[(player+1)%2]),True,WHITE)

    maSurface.blit(text, (130,810))

def Cases(maSurface, n):

    pygame.draw.rect(maSurface, GREY, (70, 60, 45, 23), 0)
    police = pygame.font.Font("freesansbold.ttf",30)

    Dimensions = police.render('Dimensions du tableau :',True ,BLUE)
    Commencer = police.render('START',True,BLUE)
    Case = police.render('<  '+str(n), True, BLUE)
    Flechedr = police.render('>', True, BLUE)
    maSurface.blit(Dimensions,(35,30))
    maSurface.blit(Case,(45,60))
    maSurface.blit(Flechedr,(120,60))
    maSurface.blit(Commencer,(571,36))

def CliqueNBCases(maSurface, n, board,start):
    x,y = event.pos
    if 45 <= x <= 62 and 68 <= y <= 86 and n>3 :
        n = n-1
        board = newBoard(n)
        return n,board,start
    if 117 <= x <= 135 and 70 <= y <= 85 and n<12 :
        n = n+1
        board = newBoard(n)
        return n,board,start
    if 572<=x<=672 and 37<=y<=61 :
        start = True
        return n,board,start
    else :
        return n,board,start

def drawLines(maSurface, lines, player,nb1):

    nb = len(lines)
    if nb1 != nb :
        nb2 = nb - nb1
        for i in range(nb2):
            if nb > 0 :
                a = lines[-1-i][0][0]
                b = lines[-1-i][0][1]
                c = lines[-1-i][1][0]
                d = lines[-1-i][1][1]
                a = a - 2
                b = b - 2
                c = c - 2
                d = d - 2
                xLines = 100 + a * taille + taille * 1 / 2
                yLines = 100 + b * taille + taille * 1 / 2
                vLines = 100 + c * taille + taille * 1 / 2
                wLines = 100 + d * taille + taille * 1 / 2
                if player == 1:
                    pygame.draw.line(maSurface, BLUE, (yLines, xLines), (wLines, vLines), 4)
                elif player == 0:
                    pygame.draw.line(maSurface, RED, (yLines, xLines), (wLines, vLines), 4)
    nb1 = nb
    return nb1

def DrawCell(maSurface,taille,i,j,l):

    if player == 1:
        police = pygame.font.Font("freesansbold.ttf", 400//n)
        LettreO = police.render('O', True, BLUE)
        LettreS = police.render('S', True, BLUE)

        if l == 1:

            pygame.draw.rect(maSurface, GREY,
            (102 + taille*(j - 2), 102 + taille*(i - 2), taille - 3, taille - 3))
            maSurface.blit(LettreS, (100 + taille * 3/10 + taille*(j - 2), 100 + taille * 3/10 + taille*(i - 2)))
        if l == 2:
            pygame.draw.rect(maSurface, GREY,
            (102 + taille * (j - 2), 102 + taille * (i - 2), taille - 3, taille - 3))
            maSurface.blit(LettreO,
            (100 + taille * 3/10 + taille * (j - 2), 100 + taille * 3/10 + taille * (i - 2)))

    if player == 0:
        police = pygame.font.Font("freesansbold.ttf", 400//n)
        LettreO = police.render('O', True, RED)
        LettreS = police.render('S', True, RED)

        if l == 1:
            pygame.draw.rect(maSurface, GREY,
            (102 + taille*(j - 2), 102 + taille*(i - 2), taille - 3, taille - 3))
            maSurface.blit(LettreS, (100 + taille * 3/10 + taille*(j - 2), 100 + taille*3/10 + taille*(i - 2)))
        if l ==2:
            pygame.draw.rect(maSurface, GREY,
            (102 + taille * (j - 2), 102 + taille * (i - 2), taille - 3, taille - 3))
            maSurface.blit(LettreO,(100 + taille * 3/10 + taille * (j - 2), 100 + taille * 3/10 + taille * (i - 2)))

def selectSquare(maSurface,taille,player):
    x,y=event.pos
    if 100 < x < 800 and 100 < y <800 :
        for a in range (0,n):
            if 100 + a*taille < y < 100 + (a+1)*taille :
                i = a + 2
        for b in range (0,n):
            if 100 + b*taille < x < 100 + (b+1)*taille :
                j = b + 2
                if 100 + b*taille+taille//2 < x < 100 + (b+1)*taille :
                    l = 2
                else :
                    l = 1
        if possibleSquare(board, n, i, j) :
            DrawCell(maSurface,taille,i,j,l)
            player = Tour(player)
            board[i][j] = l
            return i,j,l,player
    return -1,-1,-1,player

def Tour (player):
    if player == 0:
        player = player + 1
        return player
    if player == 1:
        player = player - 1
        return player

def displayWinner(maSurface,n,scores) :
    taille=n*n
    a=0
    for i in range(2,n+2):
        for j in range(2,n+2):
             if board[i][j]!=0:
                 a+=1
    if taille==a:
        if scores[0]>scores[1]:
            font = pygame.font.Font(None, 80)
            text_end = font.render('Joueur Bleu gagne!', True, BLUE)
            maSurface.blit(text_end, (810, 750))
        elif  scores[0]<scores[1]:
            font = pygame.font.Font(None, 80)
            text_end = font.render('Joueur Rouge gagne!', True, RED)
            maSurface.blit(text_end, (810, 750))
        elif  scores[0]==scores[1]:
            font = pygame.font.Font(None, 80)
            text_end = font.render('Egalité', True, WHITE)
            maSurface.blit(text_end, (1000, 750))


board = newBoard(n)
while inProgress:
    if start == False :
        taille = drawBoard(maSurface, n)
    Cases(maSurface,n)
    displayScore(maSurface,n,scores)
    displayPlayer(maSurface,n,player,joueurs)
    nb1 = drawLines(maSurface, lines, player,nb1)
    displayWinner(maSurface, n, scores)
    if start == True:
        pygame.draw.rect(maSurface, GREY, (0, 0, 400, 85), 0)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            n,board,start = CliqueNBCases(maSurface, n, board,start)
            if start == True :
                i,j,l,player = selectSquare(maSurface,taille,player)
                if l != -1:
                    score1[0]=scores[0]
                    score1[1]=scores[1]
                    update(board, n, i, j, scores, player, lines, l)
                    if scores[0]>score1[0] or scores[1]>score1[1]:
                        player = Tour(player)
        if event.type == QUIT:
            inProgress = False
    pygame.display.update()
pygame.quit()
