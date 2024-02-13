def unknown(x, y):
    """
    no idea what this code does :)
    :param x: int
    :param y: int
    :return: int
    """
    if x < y:
        print(x + y)
        return unknown(x + 1, y) * 2
    elif x == y:
        return 1
    else:
        print(x + y)
        return unknown(x - 1, y) // 2


print("Recursively: ")
print("When using 10 and 15")
print(unknown(10, 15))
print("When using 10 and 10:")
print(unknown(10, 10))
print("When using 15 and 10:")
print(unknown(15, 10))

def IterativeUnknown(x, y):
    total = 1
    if x == y:
        return 1
    if x < y:
        for i in range(y - x):
            print(x + y)
            x += 1
            total *= 2
    else:
        for i in range(x - y):
            print(x + y)
            x -= 1
            total //= 2
    return total


print("Iteratively:")
print("When using 10 and 15")
print(IterativeUnknown(10, 15))
print("When using 10 and 10:")
print(IterativeUnknown(10, 10))
print("When using 15 and 10:")
print(IterativeUnknown(15, 10))
