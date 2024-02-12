class Picture(object):
    def __init__(self, Description, Width, Height, FrameColour):
        """
        init the picture class
        :param Description: str
        :param Width: int
        :param Height: int
        :param FrameColour: str
        """
        self.Description = Description
        self.Width = Width
        self.Height = Height
        self.FrameColour = FrameColour

    def GetDescription(self):
        return self.Description

    def GetHeight(self):
        return self.Height

    def GetWidth(self):
        return self.Width

    def GetColour(self):
        return self.FrameColour

    def SetDescription(self, desc):
        self.Description = desc


picArr = [Picture("", 0, 0, "") for i in range(100)]

# def ReadData():
#     with open("./Pictures.txt", "r") as f:

