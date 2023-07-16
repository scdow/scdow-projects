import tkinter as tk
# from tkinter import *
from tkinter import messagebox
from Game import Game
from PIL import ImageTk, Image
import random
import logging
import colorlog

class GameGUI:
    def __init__(self, root):
        # Create the Game instance ...
        self.game = Game()
        self.game.createRooms()
        self.game.createRecipes()

        # Create the GUI
        # Add two menu options to the window: quit, help
        menubar = tk.Menu()
        menubar.add_command(label="Quit", command=root.destroy)
        menubar.add_command(label="Help", command=self.showHelp)
        root.config(menu=menubar)
        # self.showWelcome()   # welcome messagebox

        # create frame
        self.frame0 = tk.Frame(root, bg='#2F4F4F', width=900, height=560)
        self.frame0.pack_propagate(0)  # Prevents resizing
        self.createGUIAssets0()
        self.frame0.pack()

        self.frame1 = tk.Frame(root, bg='#2F4F4F', width=900, height=100)
        self.frame1.grid_propagate(0)  # prevents resizing
        self.createGUIAssets1()
        self.frame1.pack()

    def showWelcome(self):
        welcomeMsg = f'A dark recipe space, around the magic complex, amazing materials...\n'\
                            f'To get your recipes: Collect the materials, Mix materials in the pot.\n'\
                            f'Your command words are: help, go, kitchen, pick, drop, check, mix, quit\n'\
                            f'Control ways: etc...\n'\
                            f'(Click Help on top menu to view help info)'
        messagebox.showinfo('Welcome',f'{welcomeMsg}')
        logging.info(f'welcomeMsg:{welcomeMsg}')

    def showHelp(self):
        helpMsg = f'A dark recipe space, around the magic complex, amazing materials...\n'\
                            f'To get your recipes: Collect the materials, Mix materials in the pot.\n'\
                            f'Your command words are: help, go, kitchen, pick, drop, check, mix, quit\n'\
                            f'Bottom buttons, click open, click again close: \n'\
                                   f'check backpack, check my recipe, go kitchen, check map'
        messagebox.showinfo('Help',f'{helpMsg}')
        logging.info(f'helpMsg:{helpMsg}')

    def createGUIAssets0(self):
        # show and resize the room background
        self.roomBg = ImageTk.PhotoImage(Image.open(f'images/{self.game.currentRoom.getShortDescription()}.png').resize((900,560)))
        self.roomBgLabel = tk.Label(self.frame0, image=self.roomBg)
        self.roomBgLabel.place(x=0, y=0)

        # show room name (location)
        self.roomNameLabel = tk.Label(self.frame0, text=f'Location: {self.game.currentRoom.getShortDescription()}')
        self.roomNameLabel.place(x=20,y=10)

        # show 'mix my recipe' in kitchen
        if self.game.currentRoom==self.game.kitchen:
            self.mixBtn = tk.Button(self.frame0, text='Mix 1 to 5 materials',bg='#2f4f4f', fg='#f8f8f8',font=("arial", "12"),
                                        command=self.doMix, height=2, width=16)
            self.mixBtn.place(x=300,y=320)

        # items (materials) text in this room
        items = self.game.currentRoom.getItems()
        self.itemLabel = tk.Label(self.frame0, text=f'Materials here: {items}')
        self.itemLabel.place(x=20, y=500)
        # create list to hold an array of items
        self.itemImg = []
        self.itemBtn=[]
        for i in range(len(items)):
            self.itemImg.append(None)
            self.itemBtn.append(None)
        # show the items in room
        for i in range(len(items)):
            self.itemImg[i] = ImageTk.PhotoImage(Image.open(f'images/{items[i]}.png').resize((50,50)))
            self.itemBtn[i] = tk.Button(self.frame0, image= self.itemImg[i], command= lambda material=items[i], btn=self.itemBtn[i]: self.doPick(material,btn))
            self.itemBtn[i].place(x=random.randint(10,850),y=random.randint(10,510))  # items (materials) on random place

        # create go north (up)/south (down)/left/right button
        exits = self.game.currentRoom.getExits()
        if 'west' in exits:
            self.WestBtn = tk.Button(self.frame0, text='go west', bg='#2f4f4f', fg='#f8f8f8',
                                     relief='groove', borderwidth=2,
                                     height=2, width=8,
                                     command= lambda: self.doGo('west'))
            self.WestBtn.place(x=10, y=200)
        if 'east' in exits:
            self.EastBtn = tk.Button(self.frame0, text='go east', bg='#2f4f4f', fg='#f8f8f8',
                                     relief='groove', borderwidth=2,
                                     height=2, width=8,
                                     command=lambda: self.doGo('east'))
            self.EastBtn.place(x=820, y=200)
        if 'north' in exits:
            self.NorthBtn = tk.Button(self.frame0, text='go north', bg='#2f4f4f', fg='#f8f8f8',
                                     relief='groove', borderwidth=2,
                                     height=2, width=8,
                                     command=lambda: self.doGo('north'))
            self.NorthBtn.place(x=400, y=10)
        if 'south' in exits:
            self.SouthBtn = tk.Button(self.frame0, text='go south', bg='#2f4f4f', fg='#f8f8f8',
                                     relief='groove', borderwidth=2,
                                     height=2, width=8,
                                     command=lambda: self.doGo('south'))
            self.SouthBtn.place(x=400, y=500)
        if 'up' in exits:
            self.UpBtn = tk.Button(self.frame0, text='go up', bg='#2f4f4f', fg='#f8f8f8',
                                     relief='groove', borderwidth=2,
                                     height=2, width=8,
                                     command=lambda: self.doGo('up'))
            self.UpBtn.place(x=400, y=10)
        if 'down' in exits:
            self.DownBtn = tk.Button(self.frame0, text='go down', bg='#2f4f4f', fg='#f8f8f8',
                                   relief='groove', borderwidth=2,
                                   height=2, width=8,
                                   command=lambda: self.doGo('down'))
            self.DownBtn.place(x=400, y=500)

    def doGo(self,direction):
        self.resetGUIAssets0()
        # move to new room
        self.game.nextRoom = self.game.currentRoom.getExit(direction)
        self.game.currentRoom = self.game.nextRoom
        logging.info(f'currentRoom: {self.game.currentRoom.getShortDescription()}')
        self.createGUIAssets0()
        self.resetGUIAssets1()
        self.createGUIAssets1()

    def doMix(self):
        # button of confirm mat
        confirMat=tk.Button(self.frame0, text='Confirm Mix', bg='#2f4f4f', fg='#f8f8f8',
                                     relief='groove', borderwidth=2, font=("arial", "12"),
                                     height=2, width=16,
                                     command=self.doConfirMat)
        confirMat.place(x=300, y=320)
        # checkboxes of materials in backpack
        checkVar=[]    # store checkbox status
        checkBtn=[]
        self.checkImg=[]
        self.putMatList=[]       # list of materials to be mixed
        if len(self.game.player.backpack) > 0:
            for i in range(len(self.game.player.backpack)):
                checkVar.append(None)
                checkBtn.append(None)
                self.checkImg.append(None)
            i=0
            for mat in self.game.player.backpack:  # list of materials in backpack
                checkVar[i] = tk.IntVar()
                self.checkImg[i] = ImageTk.PhotoImage(Image.open(f'images/{mat}.png').resize((50, 50)))
                checkBtn[i] = tk.Checkbutton(self.frame0,image=self.checkImg[i],bg='#f7f7f7', text=f'{mat}',variable=checkVar[i], onvalue=1, offvalue=0,
                                               command= lambda mat=mat, btn=checkVar[i]: self.doPutMat(mat,btn))
                checkBtn[i].place(x=100+i*100, y=200)
                i+=1

    def doPutMat(self,mat,btn):
        if btn.get()==1:
            self.putMatList.append(mat)    # add mats to mixing list when checked
        else:
            self.putMatList.remove(mat)   # remove when unchecked
        # putMatLabel.config(text=f'{self.putMatList}')

    def doConfirMat(self):
        # try mix for one recipe
        mixMsg = self.game.doMixCommand(self.putMatList)
        # refresh frame0, frame1
        self.resetGUIAssets0()
        self.createGUIAssets0()
        self.resetGUIAssets1()
        self.createGUIAssets1()
        # popover of mix message
        self.mixLabel = tk.Label(self.frame0, text=f'{mixMsg}',
                                 font=("arial", "12"), bg='#2f4f4f', fg='#f8f8f8')
        self.mixLabel.place(x=100, y=100)
        self.frame0.after(2000, self.mixLabel.destroy)
        logging.info(f'mixed materials: {self.putMatList}')
        logging.info(f'mixed result: {mixMsg}')


    def doPick(self,material, btn):
        # try pick one material
        self.pickMsg = self.game.doPickCommand([material])
        # refresh frame0, frame1
        self.resetGUIAssets0()
        self.createGUIAssets0()
        self.resetGUIAssets1()
        self.createGUIAssets1()
        # popover of pick message
        self.pickLabel = tk.Label(self.frame0, text=f'{self.pickMsg}',
                                  font=("arial", "12"), bg='#2f4f4f', fg='#f8f8f8')
        self.pickLabel.place(x=100, y=100)
        self.frame0.after(2000, self.pickLabel.destroy)
        logging.info(f'pick material:{self.pickMsg}')

    def resetGUIAssets0(self):
        # reset go buttons
        # for i in self.game.currentRoom.getExits():
        #     if i == 'west':
        #         self.WestBtn.destroy()
        #     if i == 'east':
        #         self.EastBtn.destroy()
        #     if i == 'north':
        #         self.NorthBtn.destroy()
        #     if i == 'south':
        #         self.SouthBtn.destroy()
        #     if i == 'up':
        #         self.UpBtn.destroy()
        #     if i == 'down':
        #         self.DownBtn.destroy()

        # reset the all elements of frame0
        for item in self.frame0.winfo_children():
            item.destroy()

    def createGUIAssets1(self):
        # Create a suitable grid layout for bottom frame
        self.frame1.rowconfigure(0, pad=20)
        # self.frame1.rowconfigure(1, pad=10)
        for x in range(6):
            self.frame1.columnconfigure(x, pad=40)

        # Add backpack, myRecipe, goKitchen, map in frame
        self.packImg = ImageTk.PhotoImage(Image.open(f'images/backpack.png').resize((70, 70)))    # backpack button
        self.packBtn = tk.Button(self.frame1, image=self.packImg, state="normal", bg='white', command=lambda: self.doPackCheck(self.packBtn))
        self.packBtn.grid(column=0, row=0)
        self.myRecipeImg = ImageTk.PhotoImage(Image.open(f'images/myRecipe.png').resize((70, 70)))   # myRecipe button
        myRecipeBtn = tk.Button(self.frame1, image=self.myRecipeImg, state="normal",bg='white', command=lambda: self.doRecipeCheck(myRecipeBtn))
        myRecipeBtn.grid(column=1, row=0)
        self.goKitchenImg = ImageTk.PhotoImage(Image.open(f'images/kitchen.png').resize((70, 70)))  # goKitchen button
        goKitchenBtn = tk.Button(self.frame1, image=self.goKitchenImg, state="normal", bg='white', command=self.doGoKitchen)
        goKitchenBtn.grid(row=0, column=4)
        self.mapImg = ImageTk.PhotoImage(Image.open(f'images/map.png').resize((70, 70)))  # map button
        mapBtn = tk.Button(self.frame1, image=self.mapImg, state="normal", bg='white', command= lambda: self.doMap(mapBtn))
        mapBtn.grid(row=0, column=5)

    def resetGUIAssets1(self):
        # reset the all elements of frame0
        for item in self.frame1.winfo_children():
            item.destroy()

    def doMap(self,btn):
        # show map
        try:
            if btn.cget("bg")=='white':
                btn.configure(bg='#000')
                self.allMapImg = ImageTk.PhotoImage(Image.open(f'images/allMap.jpg').resize((560,560)))
                self.allMapLabel = tk.Label(self.frame0, image=self.allMapImg)
                self.allMapLabel.place(x=200, y=0)
                logging.info(f'check map')
                return
            raise AlreadyOpenError()
        # hide map
        except AlreadyOpenError:
            # refresh frame0,1
            self.resetGUIAssets0()
            self.createGUIAssets0()
            self.resetGUIAssets1()
            self.createGUIAssets1()
            logging.info('close map')
            # else:
            #     # self.allMapLabel.destroy()
            #     # btn.configure(bg='white')
            #     # refresh frame0,1
            #     self.resetGUIAssets0()
            #     self.createGUIAssets0()
            #     self.resetGUIAssets1()
            #     self.createGUIAssets1()

    def doGoKitchen(self):
        # refresh fram0
        self.resetGUIAssets0()
        self.game.currentRoom = self.game.kitchen  # go kitchen
        self.createGUIAssets0()
        # refresh frame1
        self.resetGUIAssets1()
        self.createGUIAssets1()
        logging.info(f'go kitchen')

    def doPackCheck(self,btn):
        # show backpack
        try:
            if btn.cget("bg") == 'white':
                btn.configure(bg='#000')
                # backpack bg
                self.packCheckImg = ImageTk.PhotoImage(Image.open(f'images/packCheck.png').resize((900, 140)))
                self.packCheckLabel = tk.Label(self.frame0, image=self.packCheckImg)
                self.packCheckLabel.place(x=0, y=420)
                # backpack materials
                self.pickedMatImg=[]
                self.pickedMatBtn=[]
                if len(self.game.player.backpack) > 0:
                    for i in range(len(self.game.player.backpack)):
                        self.pickedMatImg.append(None)
                        self.pickedMatBtn.append(None)
                    i=0
                    for mat in self.game.player.backpack:  # list of materials in backpack
                        self.pickedMatImg[i] = ImageTk.PhotoImage(Image.open(f'images/{mat}.png').resize((50, 50)))
                        self.pickedMatBtn[i] = tk.Button(self.frame0, image=self.pickedMatImg[i], command= lambda material=mat, btn=self.pickedMatBtn[i]: self.doDrop(material,btn))
                        self.pickedMatBtn[i].place(x=(65+i*120), y=485)
                        i+=1
                logging.info(f'check backpack:{self.game.player.backpack}')
                return
            raise AlreadyOpenError()
        # hide backpack
        except AlreadyOpenError:
            # refresh frame0,1
            self.resetGUIAssets0()
            self.createGUIAssets0()
            self.resetGUIAssets1()
            self.createGUIAssets1()
            logging.info('close backpack')
        # else:
        #     # btn.configure(bg='white')
        #     # refresh frame0, frame1
        #     self.resetGUIAssets0()
        #     self.createGUIAssets0()
        #     self.resetGUIAssets1()
        #     self.createGUIAssets1()

    def doRecipeCheck(self,btn):
        try:     # show myRecipe
            if btn.cget("bg") == 'white':
                btn.configure(bg='#000')
                # myRecipe bg
                self.recipeCheckImg= ImageTk.PhotoImage(Image.open(f'images/recipeCheck.png').resize((900, 540)))
                self.recipeCheckLabel = tk.Label(self.frame0, image=self.recipeCheckImg)
                self.recipeCheckLabel.place(x=0, y=20)
                #  myRecipe list
                self.recipeImg=[]
                self.recipeBtn=[]
                self.recipeDescripLabel=[]
                if len(self.game.myRecipe) > 0:
                    for i in range(len(self.game.myRecipe)):
                        self.recipeImg.append(None)
                        self.recipeBtn.append(None)
                        self.recipeDescripLabel.append(None)
                    i=0
                    for recipe in list(self.game.myRecipe):  # list of materials in backpack
                        # my recipe img
                        # self.recipeImg[i] = ImageTk.PhotoImage(Image.open(f'images/{self.game.myRecipe[recipe][0]}.png').resize((50, 50)))
                        self.recipeImg[i] = ImageTk.PhotoImage(Image.open(f'images/{self.game.myRecipe[recipe][0]}.png').resize((50, 50)))
                        self.recipeBtn[i] = tk.Button(self.frame0, image=self.recipeImg[i])
                        self.recipeBtn[i].place(x=120, y=120+i*80)
                        # my recipe text
                        self.recipeDescripLabel[i]= tk.Label(self.frame0, text=f'{self.game.myRecipe[recipe]}')
                        self.recipeDescripLabel[i].place(x=190, y=140+i*80)
                        i+=1
                logging.info(f'check my recipes:{self.game.myRecipe}')
                return
            raise AlreadyOpenError()
        except AlreadyOpenError:   # hide myRecipe
            # refresh frame0,1
            self.resetGUIAssets0()
            self.createGUIAssets0()
            self.resetGUIAssets1()
            self.createGUIAssets1()
            logging.info('close my recipe')
        # else:
        #     # btn.configure(bg='white')
        #     # refresh frame0, frame1
        #     self.resetGUIAssets0()
        #     self.createGUIAssets0()
        #     self.resetGUIAssets1()
        #     self.createGUIAssets1()

    def doDrop(self, material, btn):
        # try drop one material
        self.dropMsg = self.game.doDropCommand([material])
        # refresh frame0, frame1
        self.resetGUIAssets0()
        self.createGUIAssets0()
        self.resetGUIAssets1()
        self.createGUIAssets1()
        # extend backpack again
        self.doPackCheck(self.packBtn)
        # popover of pick message
        self.dropLabel = tk.Label(self.frame0, text=f'{self.dropMsg}',
                                  font=("arial", "12"), bg='#2f4f4f', fg='#f8f8f8')
        self.dropLabel.place(x=100, y=100)
        self.frame0.after(2000, self.dropLabel.destroy)
        logging.info(f'drop material: {self.dropMsg}')

class AlreadyOpenError(Exception):
    def __init__(self):
        pass

def main():
    win = tk.Tk()                           # Create a window
    win.title("Dark Recipe Adventure")                  # Set window title
    win.geometry("900x660")                 # Set window size
    win.resizable(True, True)             # Both x and y dimensions ...

    # Create the GUI as a Frame
    # and attach it to the window ...
    myApp = GameGUI(win)

    # Call the GUI mainloop ...
    win.mainloop()

def doLogging():
    # set log format, time format, log file adress, lowest log level is INFO
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(filename)s %(funcName)s %(lineno)d %(message)s',\
                        datefmt='%m/%d/%Y %I:%M:%S %p', filename='log/LogGameGUI.log',level=logging.DEBUG)
    logging.info('Started')
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')
    logging.error('Python Error')
    logging.critical('Python critical')
    # logging.log(2, 'test')
    main()  # start playing
    logging.info('Finished')

if __name__ == "__main__":
    doLogging()

