from Room import Room
from TextUI import TextUI
from Player import Player
from Recipe import Recipe

"""
    This class is the main class of the "Dark Recipe Adventure" application. 
    'Dark Recipe Adventure' is a text based adventure game.  Users 
    can walk around some scenery, collect the material, and use . 
    
    To play this game, create an instance of this class and call the "play"
    method.

    This main class creates and initialises all the others: it creates all
    rooms, creates all recipes, creates the parser and starts the game.  
    It also evaluates and executes the commands that the parser returns.
    
    This game is adapted from the 'World of Zuul' by Michael Kolling
    and David J. Barnes. The original was written in Java and has been
    simplified and converted to Python by Kingsley Sage
"""
class Game:

    def __init__(self):
        """
        Initialises the game
        """
        self.textUI = TextUI()
        self.player = Player()
        # self.createRecipes()
        self.myRecipe = {}  # to store player's own recipes

    def createRecipes(self):
        """set all recipes of game"""
        self.recipes = Recipe()
        self.recipes.setRecipe(('m1','m3','m9'),'r1_hot_fart_pot','has fart smell')
        self.recipes.setRecipe(('m2','m8'),'r2_rose_fish','can become a handsome fish')
        self.recipes.setRecipe(('m4','m5','m6'),'r3_stinky_durian_pizza','let\'s hammer the durian')
        self.recipes.setRecipe(('m2','m6','m10'),'r4_banana_peel_juice','What does banana peel taste like')
        self.recipes.setRecipe(('m4','m7'),'r5_stinky_egg_fried_rice','flies around the food')
        self.recipes.setRecipe(('m1','m3','m5','m7','m10'),'r6_eyeball_meta','eyeball is expensive')
        self.recipes.setRecipe(('m6','m6','m8'),'r7_cactus_salad','full of thorns')
        self.recipes.setRecipe(('m7',),'r8_black_ice_cream','maybe made of oil')
        self.recipes.setRecipe(('m1','m2', 'm2', 'm9'),'r9_red_crab_burger','escaped from SpongeBob SquarePants')
        self.recipes.setRecipe(('m2','m5','m6','m6','m7'),'r10_onion_watermelon','chef\'s special in university')
        self.recipes.setRecipe(('m5',), 'r11_chicken_shit', 'a chicken that looks like shit')
        self.recipes.setRecipe(('m2','m4','m6','m8','m10'), 'r12_canned_herring', 'famous for smelly')

    # def createPlayer(self):
    #     self.player = Player()

    def createRooms(self):
        """
            Sets up all room assets
        :return: None
        """
        self.kitchen = Room("in Kitchen, wow a magic pot")

        # initial location
        self.currentRoom = self.kitchen

        self.bridge = Room("on the Bridge")
        self.l1 = Room("Land1")
        self.l2 = Room("Land2")
        self.l3 = Room("Land3")
        self.l4 = Room("Land4")
        self.l5 = Room("Land5")
        self.tunnel = Room("in the sea Tunnel")
        self.s1 = Room("Sea1")
        self.s2 = Room("Sea2")
        self.s3 = Room("Sea3")
        self.s4 = Room("Sea4")

        self.kitchen.setExit("east", self.bridge)
        self.bridge.setExit("east", self.l1)
        self.bridge.setExit("west", self.kitchen)
        self.l1.setExit("east", self.l2)
        self.l1.setExit("north", self.l3)
        self.l1.setExit("west", self.bridge)
        self.l2.setExit("west", self.l1)
        self.l2.setExit("north", self.l4)
        self.l2.setExit("south", self.tunnel)
        self.l3.setExit("south", self.l1)
        self.l3.setExit("east", self.l4)
        self.l4.setExit("east", self.l5)
        self.l4.setExit("south", self.l2)
        self.l4.setExit("west", self.l3)
        self.l5.setExit("west", self.l4)
        self.tunnel.setExit("up", self.l2)
        self.tunnel.setExit("down", self.s1)
        self.s1.setExit("north", self.tunnel)
        self.s1.setExit("south", self.s3)
        self.s2.setExit("east", self.s3)
        self.s3.setExit("west", self.s2)
        self.s3.setExit("north", self.s1)
        self.s3.setExit("east", self.s4)
        self.s4.setExit("west", self.s3)

        """
        set items in specific rooms
        consider changing setItem(str) to setItem(list)
        """
        # self.kitchen.setItem('pot')
        self.l1.setItem('m1')
        # self.l2.setItem('bonus scene')
        self.l3.setItem('m2')
        self.l3.setItem('m2')
        self.l4.setItem('m3')
        self.l5.setItem('m4')
        self.l5.setItem('m5')
        self.s1.setItem('m6')
        self.s1.setItem('m6')
        self.s1.setItem('m7')
        self.s2.setItem('m9')
        self.s2.setItem('m10')
        self.s3.setItem('m8')
        # self.s3.setItem('key')
        # self.s4.setItem('shift point')
        # self.s4.setItem('bonus scene')

    def play(self):
        """
            The main play loop
        :return: None
        """
        self.printWelcome()
        # prompt starting point
        self.textUI.printtoTextUI(self.currentRoom.getLongDescription())
        finished = False
        while (finished == False):
            command = self.textUI.getCommand()      # Returns a 2-tuple
            finished = self.processCommand(command)

        print("Thank you for playing!")

    def printWelcome(self):
        """
            Displays a welcome message
        :return:
        """
        self.textUI.printtoTextUI("A dark recipe space, around the magic complex, amazing materials.")
        self.textUI.printtoTextUI("Mix materials in the pot to get your recipes.")
        self.textUI.printtoTextUI(f'Your command words are: {self.showCommandWords()}')
        self.textUI.printtoTextUI("")

    def showCommandWords(self):
        """
            Show a list of available commands
        :return: None
        """
        return ['help', 'go', 'kitchen', 'pick', 'drop', 'check', 'mix', 'quit']
        # help: describe playing ways (command)
        # go: type go [direction] , direction case sensitive
        # kitchen: shift to kitchen instantly
        # pick/drop material or key, materials case sensitive
        # mix: mix 1 to 5 material to create recipes, materials case sensitive
        # check: check the contents of backpack, the recipes created by player
        # quit: finish game

    def processCommand(self, command):
        """
            Process a command from the TextUI
        :param command: a 2-tuple of the form (commandWord, secondWord)
        :return: True if the game has been quit, False otherwise
        """
        # change: secondWord means other words
        commandWord, otherWords = command
        if commandWord != None:
            commandWord = commandWord.upper()

        wantToQuit = False
        if commandWord == "HELP":
            self.doPrintHelp()
        elif commandWord == "GO":
            self.doGoCommand(otherWords)
        elif commandWord == "KITCHEN":
            self.doKitchenCommand()
        elif commandWord == "PICK":
            self.doPickCommand(otherWords)
        elif commandWord == "DROP":
            self.doDropCommand(otherWords)
        elif commandWord == "CHECK":
            self.doCheckCommand()
        elif commandWord == "MIX":
            self.doMixCommand(otherWords)
        elif commandWord == "QUIT":
            wantToQuit = True
        else:
            # Unknown command ...
            self.textUI.printtoTextUI("Don't know what you mean")

        return wantToQuit

    def doPrintHelp(self):
        """
            Display some useful help text
        :return: None
        """
        self.textUI.printtoTextUI("A dark recipe space, around the magic complex, amazing materials.")
        self.textUI.printtoTextUI("Mix materials in the pot to get your recipes.")
        self.textUI.printtoTextUI(f'Your command words are: {self.showCommandWords()}')

    def doGoCommand(self, otherWords):
        """
            Performs the GO command
        :param secondWord: the direction the player wishes to travel in
        :return: None
        """
        # change: secondWord means other words
        if otherWords == None:
            # Missing second word ...
            self.textUI.printtoTextUI("Go where?")
            return
        # getExit: function of class Room
        # nextRoom = self.currentRoom.getExit(otherWords[0].lower())
        # """.lower(): make direction input be lower case, case insensitive"""
        nextRoom = self.currentRoom.getExit(otherWords[0])
        if nextRoom == None:
            self.textUI.printtoTextUI("There is no door!")
        else:
            self.currentRoom = nextRoom
            self.textUI.printtoTextUI(self.currentRoom.getLongDescription())

    def doKitchenCommand(self):
        self.currentRoom = self.kitchen
        self.textUI.printtoTextUI(self.currentRoom.getLongDescription())

    def doPickCommand(self, otherWords):
        """
            Performs the PICK command
        :param otherWords: otherWords[0] is the item the player wishes to pick in backpack
        :return: None
        """
        try:

            if self.player.checkPackSize() == False:
                raise FullPackError()
                # self.textUI.printtoTextUI("The backpack is full, need to drop items")
                # return
            elif otherWords == None:
                # Missing second word ...
                raise MissPickItemError()
                # self.textUI.printtoTextUI("Pick what?")
                # return
            elif otherWords[0] in self.currentRoom.getItems():
                self.player.pickItem(otherWords[0])
                self.currentRoom.removeItem(otherWords[0])
                return f'Success pick!', self.doCheckCommand()
            raise NotInRoomError()
            # else:
            #     self.textUI.printtoTextUI(f'No {otherWords[0]} here')
        except FullPackError:
            self.textUI.printtoTextUI("The backpack is full, need to drop items")
            return "The backpack is full, need to drop items"
        except MissPickItemError:
            self.textUI.printtoTextUI("Pick what?")
            return "Pick what?"
        except NotInRoomError:
            self.textUI.printtoTextUI(f'No {otherWords[0]} here')
            return f'No {otherWords[0]} here'

        # if self.player.checkPackSize() == False:
        #     raise (backpackFullError)
        #     self.textUI.printtoTextUI("The backpack is full, need to drop items")
        #     return
        # elif otherWords == None:
        #     # Missing second word ...
        #     self.textUI.printtoTextUI("Pick what?")
        #     return
        # elif otherWords[0] in self.currentRoom.getItems():
        #     self.player.pickItem(otherWords[0])
        #     self.currentRoom.removeItem(otherWords[0])
        #     self.doCheckCommand()
        # else:
        #     self.textUI.printtoTextUI(f'No {otherWords[0]} here')

    def doDropCommand(self, otherWords):
        """
            Performs the DROP command
        :param secondWord: the item the player wishes to drop out of backpack, throw in the current room
        :return: None
        """
        try:
            if otherWords == None:
                # Missing second word ...
                raise MissDropItemError()
                # self.textUI.printtoTextUI("Drop what?")
                # return
            elif otherWords[0] in self.player.backpack:
                self.player.dropItem(otherWords[0])
                self.currentRoom.addItem(otherWords[0])
                self.doCheckCommand()
                return f'Success drop!', self.doCheckCommand()
            raise NotInPackError()
            # else:
            #     self.textUI.printtoTextUI(f'no {otherWords[0]} in backpack')
        except MissDropItemError:
            self.textUI.printtoTextUI("Drop what?")
            return "Drop what?"
        except NotInPackError:
            self.textUI.printtoTextUI(f'no {otherWords[0]} in backpack')
            return f'no {otherWords[0]} in backpack'

        # if otherWords == None:
        #     # Missing second word ...
        #     self.textUI.printtoTextUI("Drop what?")
        #     return
        # elif otherWords[0] in self.player.backpack:
        #     self.player.dropItem(otherWords[0])
        #     self.currentRoom.addItem(otherWords[0])
        #     self.doCheckCommand()
        # else:
        #     self.textUI.printtoTextUI(f'no {otherWords[0]} in backpack')

    def doCheckCommand(self):
        '''check what contents in player's backpack'''
        contents = self.player.checkPack()
        self.textUI.printtoTextUI(contents)
        self.textUI.printtoTextUI(f'My recipes: {self.myRecipe}')
        return (f'{contents}',f'My recipes: {self.myRecipe}')

    def doMixCommand(self, otherWords):
        """mix 1 to 5 materials, try to cook new recipes"""
        if self.currentRoom != self.kitchen:
            self.textUI.printtoTextUI("Need go to kitchen, can type 'kitchen' to shift")
            return "Need go to kitchen, can click bottom 'kitchen' button to shift"
        elif otherWords == None:
            # Missing second word ...
            self.textUI.printtoTextUI("Mix what materials?")
            return "Mix what materials?"
        for material in otherWords:
            for item in self.player.backpack:
                if material == item:
                    break;
            else:
                self.textUI.printtoTextUI(f'No {material} in backpack')
                return f'No {material} in backpack'
        else:
            otherWords.sort()  # meterials list
            materials = otherWords
            for recipeMat in list(self.recipes.getAllMaterials()):  # recipes keys of dictionary
                recipeMatList = list(recipeMat)
                recipeMatList.sort()
                if materials == recipeMatList:
                    self.myRecipe[recipeMat] = self.recipes.getProduct(recipeMat)
                    self.textUI.printtoTextUI(f'Successfully get {self.myRecipe[recipeMat]}!')
                    self.textUI.printtoTextUI(f'you can continue play or quit')
                    """remove used materials form backpack"""
                    while materials:
                        self.player.dropItem(materials.pop())
                    return f'Successfully get {self.myRecipe[recipeMat]}!\n'\
                           f'you can continue play or quit'
            else:
                self.textUI.printtoTextUI(f'No recipe cooked, please try again~')
                return f'No recipe cooked, please try again~'

class FullPackError(Exception):
    def __init__(self):
        pass
class MissPickItemError(Exception):
    def __init__(self):
        pass
class NotInRoomError(Exception):
    def __init__(self):
        pass
class MissDropItemError(Exception):
    def __init__(self):
        pass
class NotInPackError(Exception):
    def __init__(self):
        pass

def main():
    game = Game()
    game.createRooms()
    game.createRecipes()
    game.play()

if __name__ == "__main__":
    main()