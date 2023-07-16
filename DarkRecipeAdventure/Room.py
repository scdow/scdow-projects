"""
    Create a room described "description". Initially, it has
    no exits or items. 'description' is something like 'kitchen' or
    'an open court yard'
"""
class Room:

    def __init__(self, description):
        """
            Constructor method
        :param description: text description for this room
        """
        self.description = description
        self.exits = {}     # Dictionary {direction: neighbour; ...}
        self.items = []     # List: store material, cooking tool, key in a specific room
        """
        extention: 
        items list can be changed as dictionary {'m1':2, 'm2':5},
        which can store the quantity of same item
        """

    def setExit(self, direction, neighbour):
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room)
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour
        return True

    # change: add setItem function
    # consider changing setItem(str) to setItem(list)
    def setItem(self,item):
        self.items.append(item)
        return True

    def removeItem(self,item):
        self.items.remove(item)
        return True

    def addItem(self,item):
        self.items.append(item)
        return True

    def getShortDescription(self):
        """
            Fetch a short text description
        :return: text description
        """
        return self.description

    def getLongDescription(self):
        """
            Fetch a longer description including available exits
        :return: text description, findings which include materials, cooking tool, key
        # change
        """
        if self.items:  # change: judge if items list has elements
            return f'Location: {self.description}, Exits: {self.getExits()}, Finding: {self.getItems()}'
        else:
            return f'Location: {self.description}, Exits: {self.getExits()}'

    def print_items_information(self):
        print("Items: ")
        items = ''
        for item in self.items.keys():
            items += self.items[item].name + ' '
        print(items)

    def getExits(self):
        """
            Fetch all available exits as a list
        :return: list of all available exits
        """
        allExits = self.exits.keys()
        return list(allExits)

    def getExit(self, direction):
        """
            Fetch an exit in a specified direction
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            return self.exits[direction]
            # return the neighbour room
        else:
            return None

    def getItems(self):
        """
            Fetch all items in the room
        :return: things in itmes list, divided by ', '
        """
        # return ', '.join(self.items)
        return self.items
