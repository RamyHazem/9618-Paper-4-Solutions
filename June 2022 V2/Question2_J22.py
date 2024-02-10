import random

"""
Creating a 2D array with 10 rows and colums and assigning a random number to each value
"""

data = []
for array in range(0, 10):
    new_arr = []
    for number in range(0, 10):
        random_number = random.randint(1, 100)
        new_arr.append(random_number)

    data.append(new_arr)

"""
Bubble sort algoritm on a 2D array - not the best since time complexity is O(n^2)
"""

ArrayLength = 10
for x in range(0, ArrayLength ):
    for y in range(0, ArrayLength - 1):
        for z in range(0, ArrayLength - y - 1):
            if data[x][z] > data[x][z + 1]:
                tempValue = data[x][ z]
                data[x][z] = data[x][z + 1]
                data[x][ z + 1] = tempValue


for i in range(0, 10):
    for j in range(0, 10):
        print(data[i][j], "", end="")
    print("")

