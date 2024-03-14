StackVowel = ["" for i in range(100)]  # STRING[]
StackConsonant = ["" for i in range(100)]  # STRING[]

VowelTop = 0  # INTEGER
ConsonantTop = 0  # INTEGER

vowels = ["a", "e", "i", "o", "u"]
def PushData(letter):
    global StackVowel
    global StackConsonant
    global VowelTop
    global ConsonantTop

    if VowelTop > 100:
        return "Vowel Stack is full"

    if ConsonantTop > 100:
        return "Consonant Stack is full"

    if letter in vowels:
        StackVowel[VowelTop] = letter
        VowelTop += 1
    else:
        StackConsonant[ConsonantTop] = letter
        ConsonantTop += 1


def ReadData():
    try:
        with open("./StackData.txt", "r") as f:
            for letter in f:
                PushData(letter.strip())
            f.close()
    except FileNotFoundError:
        return "Error opening file"


def PopVowel():
    global StackVowel
    global VowelTop

    if VowelTop == 0:
        return "No Data"

    value = StackVowel[VowelTop - 1]
    VowelTop -= 1
    return value


def PopConsonant():
    global StackConsonant
    global ConsonantTop

    if ConsonantTop == 0:
        return "No Data"

    value = StackConsonant[ConsonantTop - 1]
    ConsonantTop -= 1
    return value


ReadData()

answer = ""
for i in range(5):
    user = input("Choose a vowel or consonant: ")
    if user == "vowel":
        vowel = PopVowel()
        if vowel == "No Data":
            print("The stack is empty")
            break
        answer += vowel

    if user == "consonant":
        consonant = PopConsonant()
        if consonant == "No Data":
            print("The stack is empty")
            break
        answer += consonant


print(answer)

