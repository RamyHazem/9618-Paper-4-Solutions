class Card:
    def __init__(self, Number, Colour):
        self.Number = Number # INTEGER
        self.Colour = Colour # STRING

    def GetNumber(self):
        return self.Number

    def GetColour(self):
        return self.Colour


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