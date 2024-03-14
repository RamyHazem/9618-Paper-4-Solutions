import datetime


class Character(object):
    def __init__(self, CharacterName, DateOfBirth, Intelligence, Speed):
        """
        init the character class
        :param CharacterName: STRING
        :param DateOfBirth: DATE
        :param Intelligence: REAL
        :param Speed: INTEGER
        """
        self.CharacterName = CharacterName
        self.DateOfBirth = DateOfBirth
        self.Intelligence = Intelligence
        self.Speed = Speed

    def GetIntelligence(self):
        return self.Intelligence

    def GetName(self):
        return self.CharacterName

    def SetIntelligence(self, new_intelligence):
        self.Intelligence = new_intelligence

    def Learn(self):
        self.Intelligence *= 1.1

    def ReturnAge(self):
        string_DOB = str(self.DateOfBirth)
        year = string_DOB.split("-")[0]
        return 2023 - int(year)


FirstCharacter = Character(CharacterName="Royal", DateOfBirth=datetime.date(2019, 1, 19), Intelligence=70, Speed=30)
FirstCharacter.Learn()
print(
    f"Name: {FirstCharacter.GetName()}, Age: {FirstCharacter.ReturnAge()} Intelligence: {FirstCharacter.GetIntelligence()}")


class MagicCharacter(Character):
    def __init__(self, Element, CharacterName, DateOfBirth, Intelligence, Speed):
        """
        init magic character which inherits from character
        :param Element: STRING
        :param CharacterName: STRING
        :param DateOfBirth: DATE
        :param Intelligence: REAL
        :param Speed: INTEGER
        """
        super().__init__(CharacterName, DateOfBirth, Intelligence, Speed)
        self.Element = Element

    def Learn(self):
        if self.Element == "fire" or self.Element == "water":
            self.Intelligence *= 1.2
        elif self.Element == "earth":
            self.Intelligence *= 1.3
        else:
            self.Intelligence *= 1.1


FirstMagic = MagicCharacter(CharacterName="Light", DateOfBirth=datetime.date(2018,3,3), Intelligence=75, Speed=22,
                            Element="fire")

FirstMagic.Learn()
print(
    f"Name: {FirstMagic.GetName()}, Age: {FirstMagic.ReturnAge()} Intelligence: {FirstMagic.GetIntelligence()}")
