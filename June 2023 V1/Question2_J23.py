class Vehicle(object):
    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        """
        init the vehicle object
        :param ID: str
        :param MaxSpeed: int
        :param IncreaseAmount: int
        """
        self.ID = ID
        self.MaxSpeed = MaxSpeed
        self.IncreaseAmount = IncreaseAmount
        self.CurrentSpeed = 0
        self.HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.CurrentSpeed

    def GetIncreaseAmount(self):
        return self.IncreaseAmount

    def GetHorizontalPosition(self):
        return self.HorizontalPosition

    def GetMaxSpeed(self):
        return self.MaxSpeed

    def SetCurrentSpeed(self, new_speed):
        self.CurrentSpeed = new_speed

    def SetHorizontalPosition(self, new_pos):
        self.HorizontalPosition = new_pos

    def IncreaseSpeed(self):
        self.CurrentSpeed += self.IncreaseAmount
        if self.CurrentSpeed > self.MaxSpeed:
            self.CurrentSpeed = self.MaxSpeed
            self.HorizontalPosition += self.CurrentSpeed


class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, IncreaseAmount, VerticalChange, MaxHeight):
        """
        init the helicopter class - inherits from vehicle
        :param ID: str
        :param MaxSpeed: int
        :param IncreaseAmount: int
        :param VerticalChange: int
        :param MaxHeight: int
        """
        super.__init__(ID, MaxSpeed, IncreaseAmount)
        self.VerticalPosition = 0
        self.VerticalChange = VerticalChange
        self.MaxHeight = MaxHeight

    def IncreaseSpeed(self):
        self.VerticalPosition += self.VerticalChange

