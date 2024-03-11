def IterativeCalculate(number):
    total = 0
    toFind = number

    while number != 0:
        if (toFind / number).is_integer():
            total += number

        number -= 1
    return total


def RecursiveValue(number, toFind):
    if number == 0:
        return 0
    else:
        if (toFind / number).is_integer():
            return number + RecursiveValue(number - 1, toFind)
        else:
            return RecursiveValue(number - 1, toFind)


print(RecursiveValue(50, 50))