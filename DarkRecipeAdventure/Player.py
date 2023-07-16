"""
    Create a player.
    Initially, its own recipe and backpack is blank,
    can be added by Game class.
"""
class Player:
    def __init__(self):
        self.backpack=[]
        self.packSize = 7   # backpack size: max 7
        self.recipe = {}    # can store player's own recipes

    def pickItem(self,item):
        self.backpack.append(item)
        return True

    def dropItem(self,item):
        self.backpack.remove(item)
        return True

    def checkPack(self):
        # return self.backpack
        return f' Backpack contents: {self.backpack}, Size: {len(self.backpack)}/{self.packSize}'

    def checkPackSize(self):
        """return: <=7 contents in backpack,return true; otherwise, return true"""
        if len(self.backpack)<self.packSize:
            return True
        else:
            return False
