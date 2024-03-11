Queue = [0 for i in range(100)]
head_pointer = 0
tail_pointer = 0


def Enqueue(integer):
    global tail_pointer
    global Queue

    if tail_pointer < 100:
        Queue[tail_pointer] = integer
        tail_pointer += 1
        return True

    return False


for i in range(1, 21):
    result = Enqueue(i)
    if result:
        print("Successful")
    else:
        print("Unsuccessful")
print(Queue)


def RecursiveOutput(total, pointer):
    if pointer == tail_pointer:
        return total

    total += Queue[pointer]
    pointer += 1
    return RecursiveOutput(total, pointer)


print(RecursiveOutput(0, head_pointer))

