from random import choice

import viewGUI as view
import model



def getHumanTurn ():
    round=model.getRound()
    symbol=model.getHumanSymbol()
    while True:
        try:
            numTurn=int(input(f'Ход {round} ({symbol}):'))
            if (0<numTurn<10):
                if str(model.getPos(numTurn)).isdigit():
                    return numTurn
                else:
                    view.printError('Поле занято')  
            else:
                view.printError('Цифра должна быть от 1 до 9')
        except:
            view.printError('Введите цифру')



def start():
    if choice([0,1])==0:
        firstTurn=getHumanTurn
        secondTurn=model.getCompTurn
        model.setHumanSymbol('X')
    else:
        firstTurn = model.getCompTurn
        secondTurn = getHumanTurn
        model.setHumanSymbol('O')
    game=model.getGame()
    while not model.checkWin (game,'X') and not model.checkWin(game,'O') and len(model.getFreePos(game))>0:
        if model.getHumanSymbol()=='X':
            view.printGame(game, model.getHumanSymbol())
            if not model.checkWin (game,'X') and not model.checkWin(game,'O') and len(model.getFreePos(game))>0:
                model.doTurn(model.getCompTurn(),model.anotherSymbol(model.getHumanSymbol()))
        else:
            model.doTurn(model.getCompTurn(), model.anotherSymbol(model.getHumanSymbol()))
            if not model.checkWin (game,'X') and not model.checkWin(game,'O') and len(model.getFreePos(game))>0:
                view.printGame(game, model.getHumanSymbol())

        #
        # model.nextRound()
        # view.printGame (game,model.getHumanSymbol())
        # model.doTurn(firstTurn (),'X')
        # game=model.getGame()
        # if len(model.getFreePos(game))>0 and not model.checkWin(game,'X'):
        #     view.printGame (game,model.getHumanSymbol())
        #     model.doTurn(secondTurn (),'O')
        #     game=model.getGame()


    if not model.checkWin (game,'X') and not model.checkWin(game,'O'):
        view.printResult('Ничья!')
    elif model.checkWin (game,'X'):
        if model.getHumanSymbol()=='X':
            view.printResult ('Победил человек (X)')
        else:
            view.printResult('Победил бот (X)')
    else:
        if model.getHumanSymbol() == 'X':
            view.printResult('Победила бот (O)')
        else:
            view.printResult('Победил человек (O)')