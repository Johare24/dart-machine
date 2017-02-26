#Dart Scoring app written in python 3.5.2 using tkinter
#Author: John O'Hare

from tkinter import *
import random


class Window(Frame):


    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initWindow()

    def initWindow(self):
        self.master.title("Dart Machine")
        self.grid()
        self.gameType = "none"

        #Buttons
        scorePress = Button(self, text = "Submit", command = self.subScore, font='helvetica 20')
        scorePress.grid(column = 1, row = 0, padx=5, pady=5)
        #Entry initialize
        self.scoreIn = StringVar()
        self.turnScore = Entry(self, width = 3, textvariable = self.scoreIn, font='helvetica 30')
        self.turnScore.grid(column=0, row = 0)
        self.turnScore.bind("<Return>", self.onPressReturn)
        #Labels
        playerLabel = Label(self, text = "Player", font = 'helvetica 36')
        playerLabel.grid(column = 0, row = 1)
        self.pScore = StringVar()
        playerDisp = Label(self, textvariable = self.pScore, font='helvetica 30')
        playerDisp.grid(column = 1, row = 1, padx=5, pady=5)

        compLabel = Label(self, text = "Opponent", font = 'helvetica 36')
        compLabel.grid(column = 0, row = 2, padx=5, pady=5)
        self.cScore = StringVar()
        compDisp = Label(self, textvariable = self.cScore, font='helvetica 30')
        compDisp.grid(column= 1, row = 2)

        self.statusString = StringVar()
        outputDisp = Label(self, textvariable = self.statusString)
        outputDisp.grid(column=0,row=3,columnspan = 2)
        #Menus
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label = "Exit", command = self.clientExit)
        menu.add_cascade(label = "File", menu = file)

        gameBar = Menu(menu)
        gameBar.add_command(label = "Single 501", command = self.startSinglesFive)
        menu.add_cascade(label = "Games", menu = gameBar)


    def startSinglesFive(self):
        self.pScore.set("501")
        self.playerInt = 501
        self.statusString.set("Singles 501")
        self.gameType = "s501"
        self.legDart = []

        #Scores nroot.iconbitmap('')ot possible with 3 darts
        self.impossibleScores = [179, 178, 176, 175, 173, 172, 169, 166, 163, 159]
        #Finishes not possible with 3 darts
        self.impossibleFinishes = [169, 168, 166, 165, 163, 162, 159]

    def onPressReturn(self, event):
        self.subScore()

    def subScore(self):
            hit = int(self.scoreIn.get())
            proposedScore = self.playerInt - hit

            #Player enters a score not possible in three darts
            if(hit > 180 or (hit in self.impossibleScores)):
                self.statusString.set("Score not possible")
            #Player enters a score which will bust them
            elif(proposedScore < 0 or proposedScore == 1):
                self.statusString.set("Player has bust")
                self.legDart.append(0)
            #Normal scoring conditions (no bust and score is possible)
            elif(proposedScore > 1):
                self.playerInt = proposedScore
                self.pScore.set(str(proposedScore))
                self.legDart.append(hit)
            #Player has entered a score which will result in a finish if valid
            elif(proposedScore == 0):
                #player enters invalid finish
                if (hit in self.impossibleFinishes or hit > 170):
                    self.statusString.set("Finish not possible")
                #player finishes with valid score
                else:
                    self.statusString.set("Player has won the leg")
                    self.playerInt = proposedScore
                    self.pScore.set(str(proposedScore))
                    self.legDart.append(hit)
                    self.writeLeg(self.legDart, 3)
            #unforseen case
            else:
                self.statusString.set("Enter a valid score")
            self.turnScore.delete(0, END)

    def writeLeg(self, leg, finish):
        print(sum(leg)/len(leg))

    def clientExit(self):
        self.master.destroy()

root = Tk()
#root.geometry("300x200")

app = Window(root)

root.mainloop()
