Animals = ["" for i in range(10)]
Animals = ["horse", "lion", "rabbit", "mouse", "bird", "deer", "whale", "elephant", "kangaroo", "tiger"]


def SortDescending():
    ArrayLength = len(Animals)
    for x in range(ArrayLength - 1):
        for y in range(ArrayLength - x - 1):
            if Animals[y][0] < Animals[y + 1][0]:
                Animals[y], Animals[y + 1] = Animals[y + 1], Animals[y]


SortDescending()
for animal in Animals:
    print(animal)
