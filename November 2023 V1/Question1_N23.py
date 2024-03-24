vowels = ["a", "e", "i", "o", "u"]

def IterativeVowels(value: str):
    total = 0

    for x in range(0, len(value)):
        first_character = value[0]
        if first_character.lower() in vowels:
            total += 1

        value = value[1: len(value)]

    return total

# print(IterativeVowels("house"))


def RecursiveVowels(value: str):

    if value == "":
        return 0

    if value[0].lower() in vowels:
        return 1 + RecursiveVowels(value[1: len(value)])
    else:
        return RecursiveVowels(value[1: len(value)])


print(RecursiveVowels("imagine"))
