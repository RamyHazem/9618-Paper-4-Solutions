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


ReadFile()
print(DataArray)