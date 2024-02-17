class Balloon(object):
    def __init__(self, Colour, DefenceItem):
        """
        init the balloon obj
        :param Colour: str
        :param DefenceItem: str
        """
        self.Colour = Colour
        self.DefenceItem = DefenceItem
        self.Health = 100

    def GetDefenceItem(self):
        return self.DefenceItem

    def ChangeHealth(self, num):
        self.Health += num

    def CheckHealth(self):
        if self.Health <= 0:
            return True
        return False


user_defence_item = input("Please enter the balloon's defence item: ")
user_colour = input("Please enter the balloon's colour: ")
new_balloon_obj = Balloon(user_colour, user_defence_item)

def Defend(balloon_obj):
    """
    defend against opponent
    :param balloon_obj: Balloon
    :return: Balloon
    """
    while True:
        opp_strength = input("Please enter the opponent's strength: ")
        if opp_strength.isdigit():
            opp_strength = int(opp_strength)
            break

    balloon_obj.ChangeHealth(-opp_strength)
    print(f"The defence item of the balloon: {balloon_obj.GetDefenceItem()}")

    if balloon_obj.CheckHealth():
        print("No health remaining.. You Lost! ")
    else:
        print(f"Remaining Health: {balloon_obj.Health}")

    return balloon_obj


Defend(new_balloon_obj)