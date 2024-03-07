DataArray = []

try:
    with open("./Data.txt", "r") as f:
        for line in f:
            DataArray.append(int(line.strip()))
except FileNotFoundError:
    print("Error opening file")


def PrintArray(arr):
    str = ""
    for num in arr:
        str += f"{num} "

    return str


def LinearSearch(arr, value):
    count = 0
    for num in arr:
        if num == value:
            count += 1

    return count


while True:
    user_num = input("Please enter a number between 1 and 100: ")
    if user_num.isdigit():
        user_num = int(user_num)
        if 1 <= user_num <= 100:
            count = LinearSearch(DataArray, user_num)
            print(f"The number {user_num} is found {count} times")
            break
        print("Number out of range - must be between 1 and 100")
    print("Input is not a valid number")
