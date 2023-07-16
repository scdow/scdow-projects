import re
"""
    A simple text based User Interface (UI) for the
    Adventure World game
"""

class TextUI:

    def __init__(self):
        # Nothing to do ...
        pass

    def getCommand(self):
        """
            Fetches a command from the console
        :return: a 2-tuple of the form (commandWord, secondWord), means (first word, other words list)
        """
        word1 = None
        otherWords = None
        print('> ', end='')
        inputLine = input()
        if inputLine != "":
            # allWords = inputLine.split()
            allWords = re.split(r'(?:\s+|,)', inputLine)
            """split by , and blank"""
            allWords = [item for item in filter(lambda x: x != '', allWords)]
            """delete ''   """
            word1 = allWords[0]
            if len(allWords) > 1:
                # word2 = allWords[1]
                # """before: Just ignore any other words"""
                del(allWords[0])
                # word2 = ' '.join(allWords)
                otherWords = allWords
                """change: otherWords = all words after word1"""
            else:
                otherWords = None
        return (word1, otherWords)
        # 2 - tuple
    def printtoTextUI(self, text):
        """
            Displays text to the console
        :param text: Text to be displayed
        :return: None
        """
        print(text)
