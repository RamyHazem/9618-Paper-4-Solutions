Animal = ["" for i in range(20)]
Colour = ["" for i in range(10)]

AnimalTopPointer = 0
ColourTopPointer = 0


def PushAnimal(DataToPush):
    """
    push a new animal to the animal array
    :param DataToPush: str
    :return: bool
    """
    global AnimalTopPointer
    global Animal

    if AnimalTopPointer == 20:
        return False

    Animal[AnimalTopPointer] = DataToPush
    AnimalTopPointer += 1
    return True


def PopAnimal():
    """
    pop an animal from the stack
    :return: str
    """
    global AnimalTopPointer
    global Animal

    if AnimalTopPointer == 0:
        return ""

    ReturnData = Animal[AnimalTopPointer - 1]
    AnimalTopPointer -= 1
    return ReturnData


def ReadData():
    try:
        with open("./AnimalData.txt", "r") as animal_file:
            for line in animal_file:
                PushAnimal(line.strip())
        animal_file.close()

        with open("./ColourData.txt", "r") as colour_file:
            for line in colour_file:
                PushColour(line.strip())
        colour_file.close()

    except FileNotFoundError:
        return "Error opening file"


def PushColour(DataToPush):
    """
    push a new colour to the colours array
    :param DataToPush: str
    :return: bool
    """
    global ColourTopPointer
    global Colour

    if ColourTopPointer == 20:
        return False

    Colour[ColourTopPointer] = DataToPush
    ColourTopPointer += 1
    return True


def PopColour():
    """
    pop a colour from the stack
    :return: str
    """
    global ColourTopPointer
    global Colour

    if ColourTopPointer == 0:
        return ""

    ReturnData = Colour[ColourTopPointer - 1]
    ColourTopPointer -= 1
    return ReturnData


def OutputItem():
    animal = PopAnimal()
    colour = PopColour()
    if animal and colour:
        return f"{colour} {animal}"
    elif animal and not colour:
        PushAnimal(animal)
        return "No Colour"
    else:
        PushColour(colour)
        return "No Animal"


ReadData()
print(OutputItem())
print(OutputItem())
print(OutputItem())
print(OutputItem())