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


