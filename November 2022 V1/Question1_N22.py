DataArray = []


def ReadFile():
    global DataArray
    try:
        with open("./IntegerData.txt", "r") as f:
            for i in range(100):
                num = int(f.readline().strip())
                DataArray.append(num)
            f.close()
    except FileNotFoundError:
        return "File not found"


def FindValues():
    count = 0
    while True:
        num_to_search = input("Please enter a number to search in the array: ")
        if num_to_search.isdigit():
            num_to_search = int(num_to_search)
            break
        else:
            print("Value inputted is not a valid number, try again. ")

    if 1 <= num_to_search <= 100:
        for num in DataArray:
            if num_to_search == num:
                count += 1

    return count, num_to_search


ReadFile()
no_of_appearances, value = FindValues()
print(f"The value {value} was found {no_of_appearances} times! ")


def BubbleSort():
    for i in range(len(DataArray)):
        for y in range(len(DataArray) - 1):
            if DataArray[y] > DataArray[y + 1]:
                DataArray[y + 1], DataArray[y] = DataArray[y], DataArray[y + 1]

    return DataArray


print(BubbleSort())

