QueueArray = ["" for i in range(10)]  # String[]
head_pointer = 0  # Integer
tail_pointer = 0  # Integer
no_of_items = 0  # Integer


def Enqueue(DataToAdd):
    global QueueArray
    global head_pointer
    global tail_pointer
    global no_of_items
    """
    add data to the queue
    :param DataToAdd: str
    :return: bool
    """

    if no_of_items == 10:
        return False

    QueueArray[tail_pointer] = DataToAdd
    if tail_pointer >= 9:
        tail_pointer = 0
    else:
        tail_pointer += 1

    no_of_items += 1
    return True


def Dequeue():
    global QueueArray
    global head_pointer
    global tail_pointer
    global no_of_items

    if no_of_items == 0:
        return False

    nextDataItem = QueueArray[head_pointer]
    if head_pointer < 9:
        head_pointer += 1
        return nextDataItem


for i in range(11):
    item_to_add = input("Add an item to the queue: ")
    if Enqueue(item_to_add):
        print("item successfully added to the queue")
    else:
        print("the queue is full")

print(Dequeue())
print(Dequeue())