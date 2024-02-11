class TreasureChest(object):
    def __init__(self, question, answer, points):
        """
        :param question: str
        :param answer: int
        :param points: int
        """
        self.question = question
        self.answer = int(answer)
        self.points = int(points)

    def getQuestion(self):
        """
        returns the current question
        :return:str
        """
        return self.question

    def checkAnswer(self, user_answer):
        """
        check if the user's answer is correct
        :param user_answer: int
        :return: bool
        """
        if user_answer == self.answer:
            return True
        return False

    def getPoints(self, no_of_attempts):
        """
        returns the number of points the user earns for answering this question
        :param no_of_attempts: int
        :return: int
        """
        if no_of_attempts == 1:
            return self.points
        elif no_of_attempts == 2:
            return self.points / 2
        elif no_of_attempts == 3 or no_of_attempts == 4:
            return self.points / 4
        else:
            return 0


arrayTreasure = []  # Type TreasureChest


def readData():
    try:
        file = open("./TreasureChestData.txt", "r")
        for i in range(5):
            question = file.readline()
            answer = file.readline()
            points = file.readline()
            newTreasureChest = TreasureChest(question, answer, points)
            arrayTreasure.append(newTreasureChest)
        file.close()
    except FileNotFoundError:
        print("File not found!")


readData()
questionNo = int(input("Enter a number between 1 and 5: "))
currentChestObj = arrayTreasure[questionNo - 1]
print(f"The question is: {currentChestObj.getQuestion()}")
user_input_answer = int(input("Type in your answer:"))
user_guesses = 1
while not currentChestObj.checkAnswer(user_input_answer):
    print("Wrong answer! try again")
    user_input_answer = int(input(f"The question is: {currentChestObj.getQuestion()}Type in your answer:"))
    user_guesses += 1

points_earned = int(currentChestObj.getPoints(user_guesses))
print(f"You earned {points_earned} points for answering this question correctly!")
