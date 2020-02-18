scores = [0,0]
player = 0
joueurs = ("bleu", "rouge")
lines = []
def newBoard(n):
    liste = []
    for i in range(n+4):
        liste2 = []
        for j in range(n+4):
            liste2.append(0)
        liste.append(liste2)
    return liste

def possibleSquare(board,n,i,j):
    if board[i][j] == 0 and 2 <= i <= n+2 and 2 <= j <= n+2:
        return True
    else:
        return False

def updateScoreS(board,n,i,j,scores,player,lines):
    if board[i-1][j-1] == 2 and board[i-2][j-2] == 1:
        scores[player] += 1
        lines.append([(i-2,j-2),(i,j)])
    if board[i-1][j] == 2 and board[i-2][j] == 1:
        scores[player] += 1
        lines.append([(i - 2, j), (i, j)])
    if board[i-1][j+1] == 2 and board[i-2][j+2] == 1:
        scores[player] += 1
        lines.append([(i - 2, j + 2), (i, j)])
    if board[i][j+1] == 2 and board[i][j+2] == 1:
        scores[player] += 1
        lines.append([(i, j + 2), (i, j)])
    if board[i+1][j+1] == 2 and board[i+2][j+2] == 1:
        scores[player] += 1
        lines.append([(i + 2, j + 2), (i, j)])
    if board[i+1][j] == 2 and board[i+2][j] == 1:
        scores[player] += 1
        lines.append([(i + 2, j), (i, j)])
    if board[i+1][j-1] == 2 and board[i+2][j-2] == 1:
        scores[player] += 1
        lines.append([(i + 2, j - 2), (i, j )])
    if board[i][j-1] == 2 and board[i][j-2] == 1:
        scores[player] += 1
        lines.append([(i, j - 2), (i, j)])

def updateScoreO(board,n,i,j,scores,player,lines):
    if board[i-1][j-1] == 1 and board[i+1][j+1] == 1:
        scores[player]+=1
        lines.append([(i - 1, j - 1), (i + 1, j + 1)])
    if board[i-1][j+1] == 1 and board[i+1][j-1] == 1:
        scores[player]+=1
        lines.append([(i - 1, j + 1), (i + 1, j - 1)])
    if board[i-1][j] == 1 and board[i+1][j] == 1:
        scores[player]+=1
        lines.append([(i - 1, j), (i + 1, j)])
    if board[i][j-1] == 1 and board[i][j+1] == 1:
        scores[player]+=1
        lines.append([(i, j - 1), (i, j + 1)])

def update(board,n,i,j,scores,player,lines,l):
    board[i][j] = l
    if board[i][j] == 1 :
        updateScoreS(board,n,i,j,scores,player,lines)
    elif board[i][j] == 2 :
        updateScoreO(board, n, i, j, scores, player, lines)

def winner(scores):
    print("Partie terminée, score du joeur 1: ", scores[0], "score du joueur 2: ", scores[1])

