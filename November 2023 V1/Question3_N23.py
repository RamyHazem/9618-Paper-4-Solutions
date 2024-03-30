class Character(object):
    def __init__(self, Name, XPosition, YPosition):
        """
        init the class
        :param Name: STRING
        :param XPosition: INTEGER
        :param YPosition: INTEGER
        """
        self.Name = Name
        self.XPosition = XPosition
        self.YPosition = YPosition

    def GetXPosition(self):
        return self.XPosition

    def GetYPosition(self):
        return self.YPosition

    def SetXPosition(self, value):
        if self.XPosition + value > 10000:
            self.XPosition = 10000
        elif self.XPosition + value < 0:
            self.XPosition = 0
        self.XPosition += value

    def SetYPosition(self, value):
        if self.YPosition + value > 10000:
            self.YPosition = 10000
        elif self.YPosition + value < 0:
            self.YPosition = 0
        self.YPosition += value

    def Move(self, direction):
        if direction == "up":
            self.SetYPosition(10)
        elif direction == "down":
            self.SetYPosition(-10)
        elif direction == "left":
            self.SetXPosition(-10)
        elif direction == "right":
            self.SetXPosition(10)


Jack = Character(Name="Jack", XPosition=50, YPosition=50)


class BikeCharacter(Character):
    def __init__(self, Name, XPosition, YPosition):
        """
        init the class
        :param Name: STRING
        :param XPosition: INTEGER
        :param YPosition: INTEGER
        """
        super().__init__(Name, XPosition, YPosition)

    def Move(self, direction):
        if direction == "up":
            self.SetYPosition(20)
        elif direction == "down":
            self.SetYPosition(-20)
        elif direction == "left":
            self.SetXPosition(-20)
        elif direction == "right":
            self.SetXPosition(20)


Karla = BikeCharacter(Name="Karla", XPosition=100, YPosition=50)

while True:
    choice = input("Please choose a character to move: Karla or Jack: ").lower()
    if choice == "karla" or choice == "jack":
        direction = input(f"Please choose a direction for {choice} to move: [Up/Down/Left/Right]: ").lower()
        directions = ["up", "down", "left", "right"]
        if direction in directions:
            if choice == "karla":
                Karla.Move(direction)
                print(f"Karla's new position is X = {Karla.GetXPosition()} Y = {Karla.GetYPosition()}")
            else:
                Jack.Move(direction)
                print(f"Jack's new position is X = {Jack.GetXPosition()} Y = {Jack.GetYPosition()}")
            break

        else:
            print("Invalid Direction, try again!")

    else:
        print("Invalid name, try again!")

