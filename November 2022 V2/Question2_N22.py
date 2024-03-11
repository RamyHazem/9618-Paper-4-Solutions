class Character(object):
    def __init__(self, name, x_coordinate, y_coordinate):
        """
        init the character class
        :param name: str
        :param x_coordinate: int
        :param y_coordinate: int
        """
        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def GetName(self):
        return self.name

    def GetX(self):
        return self.x_coordinate

    def GetY(self):
        return self.y_coordinate

    def ChangePosition(self, new_x, new_y):
        self.x_coordinate += new_x
        self.y_coordinate += new_y


characters = []

# opening the file

try:
    with open("./Characters.txt") as f:
        while True:
            name = f.readline().strip().lower()
            if name == "":
                break
            x_coord = int(f.readline().strip())
            y_coord = int(f.readline().strip())
            character_obj = Character(name=name, x_coordinate=x_coord, y_coordinate=y_coord)
            characters.append(character_obj)

except FileNotFoundError:
    print("error opening file")

character_index = 0

while True:
    user_name = input("Please enter a name to search: ").lower()
    for char in characters:
        if char.GetName() == user_name:
            character_index = characters.index(char)
            print(character_index)
            break
    else:
        print("Not a valid name")
        continue
    break

while True:
    legal_moves = ["w", "a", "s", "d"]
    move = input("Please enter a move for the character to do: [W/A/S/D] ").lower()
    if move in legal_moves:
        if move == "w":
            characters[character_index].ChangePosition(0, 1)
        elif move == "a":
            characters[character_index].ChangePosition(-1, 0)
        elif move == "s":
            characters[character_index].ChangePosition(0, -1)
        else:
            characters[character_index].ChangePosition(1, 0)
        print(f"{user_name} has changed coordinates to X = {characters[character_index].GetX()} and Y = {characters[character_index].GetY()}")
        break
    else:
        print("Not a valid move")
