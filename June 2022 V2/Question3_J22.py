class Card:

    def __init__(self, Number, Colour):
        """
        :param Number: int
        :param Colour: str
        """
        self.Number = Number
        self.Colour = Colour


    def GetNumber(self):
        """
        getter method for returning the number
        :return: int
        """
        return self.Number

    def GetColour(self):
        """
        getter method for returing the color
        :return: str
        """
        return self.Colour


"""
Reading data from the CardValues file and adding them to the cards array
"""

cards = []  # Integer
try:
    file = open("./CardValues.txt", "r")
    for i in range(0, 30):
        number = int(file.readline())
        color = file.readline()
        new_card = Card(number, color)
        cards.append(new_card)
except FileNotFoundError:
    print("File doesn't exist")

selected_indexes = []


def ChooseCard():
    """
    Choosing a random card from the cards array and returing its index
    :return: int
    """
    global selected_indexes
    index = int(input("Please enter an index from 1 to 30: "))
    if 1 > index > 30:
        print("Index out of range! ")

    if index not in selected_indexes:
        selected_indexes.append(index)
        return index


Player1 = []

for i in range(0, 4):
    cardIndex = ChooseCard()
    Player1.append(cards[cardIndex])

for i in range(0, len(Player1)):
    print(Player1[i].Number, Player1[i].Colour)