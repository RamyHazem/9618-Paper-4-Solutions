arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


def linearSearch(integer):
    """
    performs a linear search on the arrayData array
    :param integer: int
    :return: bool
    """
    for num in arrayData:
        if integer == num:
            return True
    return False


while True:
    user_input = input("Please enter a number to check if its in the array: ")
    if user_input.isdigit():
        user_input = int(user_input)
        break

if linearSearch(user_input):
    print("The value was found in the array! ")
else:
    print("The value is not in the array")


def bubbleSort():
    for x in range(len(arrayData)):
        for y in range(len(arrayData) - 1):
            if arrayData[y] > arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp


bubbleSort()
print(arrayData)
