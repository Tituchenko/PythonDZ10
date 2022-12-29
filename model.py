from random import choice
winPositions=({1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}) # выигрышые позиции
game =[x for x in range(1,10)]
round=0
symbol=''

def nextRound():
    global round
    round+=1

def doTurn(n,s):
    global game
    game [n-1]=s

def getGame():
    global game
    return game
def getRound():
    global round
    return round

def setHumanSymbol(s):
    global symbol
    symbol=s


def getHumanSymbol():
    global symbol
    return symbol

def getPos (n):
    global game
    return game[n-1]

def getPosition (game,symbol): #Возвращает список занятых symbol позиций
    return  [i+1 for i,x in enumerate(game) if x==symbol]

def anotherSymbol (symbol):
    if symbol=='X':
        return 'O'
    else:
        return 'X'

def checkWin (game,symbol):
    global winPositions
    pos=getPosition(game,symbol)
    for wp in winPositions:
        if wp.issubset(pos):
            return True
    return False

def getCurWinPosition (game,symbol):
    # возвращает список ->
    # [0]-список множеств, по которым еще можно выиграть с учетом текущих позиций противника.
    # [1]-сколько в этих множеств наших позиций
    curPos=[]
    curPosHasMy=[]
    posAnother=getPosition (game,anotherSymbol(symbol))
    posMy = getPosition(game, symbol)
    for wp in winPositions:
        for p in posAnother:
            if p in wp:
                break
        else:
            hasMy=0
            for p in posMy:
                if p in wp:
                   hasMy+=1
                   wp.remove(p)
            curPos.append(wp)
            curPosHasMy.append(hasMy)
    return curPos,curPosHasMy

def getFreePos (game):# возвращает свободные позиции
    return [x for x in range (1,10) if str(game[x-1]).isdigit()]

def checkNextTurnWin (game,symbol): # проверяет можно ли победить symbol следующим ходом
    freePos = getFreePos(game)
    for i in freePos:
        gameTemp=game.copy()
        gameTemp[i-1]=(symbol)
        if checkWin (gameTemp,(symbol)):
            return i
    else:
        return 0

def getCompTurn (): # ход компьютера
    # Проверим можем ли победить
    global game
    global symbol
    global curWinPosition
    s=anotherSymbol(symbol)
    checkMy=checkNextTurnWin(game,s)
    if checkMy>0:
        # print(f'Ход {round} ({s}):{checkMy}')
        return checkMy
    # Проверим может ли соперник победить следующим
    checkOpponent=checkNextTurnWin(game,symbol)
    if checkOpponent>0:
        # print(f'Ход {round} ({symbol}):{checkOpponent}')
        return checkOpponent
    # иначе вытащим возможные ходы, входящие в выигрышные на текущий момент комбинации
    curWinPosition=getCurWinPosition(game,s)
    realTurn=set()
    realTurnInWin=[0]*10
    for i in range(0,len(curWinPosition[1])):
        # в ходах в выигрышных комбинациях оставим только те, в которых уже есть наши ходы максимально
        if curWinPosition[1][i]==max(curWinPosition[1]):
            realTurn.update(list(curWinPosition[0][i]))
            # посчитаем также в скольких выигрышных комбинациях есть возможные ходы (увеличиваем шанс вилки!)
            for j in curWinPosition[0][i]:
                realTurnInWin[j]+=1

    if len (realTurn)>0:
        realTurnMaxInWin=set()
        for rt in realTurn:
            if realTurnInWin[rt]==max(realTurnInWin):
                realTurnMaxInWin.add(rt)
        turn=choice(list(realTurnMaxInWin))

    else:
        turn=choice(getFreePos(game))
    # print (f'Ход {round} ({s}):{turn}')
    return turn
