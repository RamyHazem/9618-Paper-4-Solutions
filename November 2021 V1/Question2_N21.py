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

def ReadData():
    counter = 0
    try:
        with open("./Pictures.txt", "r") as f:
            description = f.readline().strip()
            while description != "":
                height = int(f.readline().strip())
                width = int(f.readline().strip())
                colour = f.readline().strip()
                picArr[counter] = Picture(description, height, width, colour)
                counter += 1
                description = f.readline().strip()

            f.close()
    except FileNotFoundError:
        return "File not found!"

    return counter


print(ReadData())

frameColourReq = input("Please enter the colour of the frame of the picture: ").lower()
maxWidthReq = int(input("Please enter the maximum width of the picture: "))
maxHeightReq = int(input("Please enter the maximum height of the picture: "))

print("Results: ")
for pic in picArr:
    if pic.GetColour() == frameColourReq and pic.GetWidth() <= maxWidthReq and pic.GetHeight() <= maxHeightReq:
        print(f"Description: {pic.GetDescription()}, Width: {pic.GetWidth()}, Height: {pic.GetHeight()}")

