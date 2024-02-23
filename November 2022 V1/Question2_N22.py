class Card(object):
    def __init__(self, Number, Colour):
        """
        init the card class
        :param Number: int
        :param Colour: str
        """
        self.Number = Number
        self.Colour = Colour

    def GetNumber(self):
        return self.Number

    def GetColour(self):
        return self.Colour


class Hand(object):
    def __init__(self, Card1, Card2, Card3, Card4, Card5):

        self.Cards = []

        self.Cards.append(Card1)
        self.Cards.append(Card2)
        self.Cards.append(Card3)
        self.Cards.append(Card4)
        self.Cards.append(Card5)

        self.FirstCard = 0
        self.NumberCards = 5

    def GetCard(self, index):
        return self.Cards[index]


red1 = Card(1, "red")
red2 = Card(2, "red")
red3 = Card(3, "red")
red4 = Card(4, "red")
red5 = Card(5, "red")

blue1 = Card(1, "blue")
blue2 = Card(2, "blue")
blue3 = Card(3, "blue")
blue4 = Card(4, "blue")
blue5 = Card(5, "blue")

yellow1 = Card(1, "yellow")
yellow2 = Card(2, "yellow")
yellow3 = Card(3, "yellow")
yellow4 = Card(4, "yellow")
yellow5 = Card(5, "yellow")


Player1Hand = Hand(red1, red2, red3, red4, yellow1)
Player2Hand = Hand(yellow2, yellow3, yellow4, yellow5, blue1)

def CalculateValue(player_hand):
    score = 0
    for i in range(5):
        currentCard = player_hand.GetCard(i)
        currentColour = currentCard.GetColour()
        currentNumber = int(currentCard.GetNumber())
        score += currentNumber
        if currentColour == "red":
            score += 5
        elif currentColour == "blue":
            score += 10
        else:
            score += 15
    return score

player_1_score = CalculateValue(Player1Hand)
player_2_score = CalculateValue(Player2Hand)

if player_1_score > player_2_score:
    print(f"Player 1 is the winner! {player_1_score} vs {player_2_score}")
elif player_1_score == player_2_score:
    print(f"The game was a draw! {player_1_score} vs {player_2_score} ")
else:
    print(f"Player 2 is the winner! {player_2_score} vs {player_1_score}")