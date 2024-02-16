player_names = []
player_scores = []


def ReadHighScores():
    """
    read data from the file and store them in the arrays declared
    :return: None
    """
    try:
        with open("./HighScore.txt", "r") as f:
            name = f.readline().strip()
            while name != "":
                score = int(f.readline().strip())
                player_names.append(name)
                player_scores.append(score)
                name = f.readline().strip()
        f.close()
        print("Data read successfully!")
        return
    except FileNotFoundError:
        print("File not found")
        return


def OutputHighScores():
    for i in range(len(player_names)):
        print(player_names[i], player_scores[i])


ReadHighScores()
OutputHighScores()

# This code is for validation of the new name [3 characters]
while True:
    new_name = input("Please enter a new 3-character player name: ")
    if len(new_name) == 3:
        break
    else:
        print("Player name must be 3 characters, try again.")

# This code is for validation of the new score [first make sure it's a valid number and then make sure it's within the
# given range)

while True:
    new_score = input("Please enter the player's score [must be between 1 and 10000]:")
    if new_score.isdigit():
        new_score = int(new_score)
        if 1 <= new_score <= 10000:
            break
        else:
            print("Score entered is not between 1 and 10000, try again.")
    else:
        print("Score entered is not a valid score, try again.")


def make_new_list(name, score):
    for i in range(len(player_scores)):
        if score > player_scores[i]:
            player_scores.insert(i, score)
            player_names.insert(i, name)
            return

    for i in range(0, 10):
        print(player_names[i], player_scores[i])


print("Contents before inserting: ")
print(player_names)
print(player_scores)

make_new_list(new_name, new_score)

print("Contents after inserting: ")
print(player_names)
print(player_scores)


def WriteTopTen():
    with open("NewHighScores.txt", "x") as f:
        for i in range(0, 10):
            f.write(f"{player_names[i]}\n")
            f.write(f"{player_scores[i]}\n")

        print("file created! ")


WriteTopTen()
