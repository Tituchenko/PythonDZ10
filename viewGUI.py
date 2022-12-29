from tkinter import *
from tkinter import messagebox

def pressButton (num,game,symbol):
    if str(game[num]).isdigit():
        game[num]=symbol
        window.destroy()


def printResult(txt):
    messagebox.showinfo("Результат:", txt)

def printGame (game,symbol):
    global window
    window= Tk()
    window.title("XO game")
    window.geometry('200x310')
    # i=0
    btn=[]
    # for r in range (0,3):
    #     for c in range (0,3):
    #         btn.append( Button(window, text=game[i], width=3,height=2,font=("Arial Bold", 25),command= lambda:pressButton(i)))
    #         btn[i].grid(column=c, row=r)
    #         i+=1
    btn.append(Button(window, text=game[0], width=3, height=2, font=("Arial Bold", 25), command=lambda: pressButton(0,game,symbol)))
    btn[0].grid(column=0, row=0)

    btn.append(Button(window, text=game[1], width=3, height=2, font=("Arial Bold", 25), command=lambda: pressButton(1,game,symbol)))
    btn[1].grid(column=1, row=0)

    btn.append(Button(window, text=game[2], width=3, height=2, font=("Arial Bold", 25), command=lambda: pressButton(2,game,symbol)))
    btn[2].grid(column=2, row=0)

    btn.append(Button(window, text=game[3], width=3, height=2, font=("Arial Bold", 25), command=lambda: pressButton(3,game,symbol)))
    btn[3].grid(column=0, row=1)

    btn.append(Button(window, text=game[4], width=3, height=2, font=("Arial Bold", 25), command=lambda: pressButton(4,game,symbol)))
    btn[4].grid(column=1, row=1)

    btn.append(Button(window, text=game[5], width=3, height=2, font=("Arial Bold", 25), command=lambda: pressButton(5,game,symbol)))
    btn[5].grid(column=2, row=1)

    btn.append(Button(window, text=game[6], width=3, height=2, font=("Arial Bold", 25), command=lambda: pressButton(6,game,symbol)))
    btn[6].grid(column=0, row=2)

    btn.append(Button(window, text=game[7], width=3, height=2, font=("Arial Bold", 25), command=lambda: pressButton(7,game,symbol)))
    btn[7].grid(column=1, row=2)

    btn.append(Button(window, text=game[8], width=3, height=2, font=("Arial Bold", 25), command=lambda: pressButton(8,game,symbol)))
    btn[8].grid(column=2, row=2)
    window.mainloop()




def printError(text):
    print(text)