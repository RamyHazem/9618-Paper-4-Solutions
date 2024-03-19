class SaleData(object):
    def __init__(self, ID, quantity):
        self.ID = ID
        self.quantity = quantity


CircularQueue = [SaleData("", -1) for i in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0


def Enqueue(record):
    global Tail, NumberOfItems

    if NumberOfItems == 5:
        return -1
    CircularQueue[Tail] = record
    Tail = (Tail + 1) % 5
    NumberOfItems += 1
    return 1


def Dequeue():
    global Head, NumberOfItems

    if NumberOfItems == 0:
        return SaleData("null", -1)

    first_item = CircularQueue[Head]
    Head = (Head + 1) % 5
    NumberOfItems -= 1
    return first_item


def EnterRecord():
    ID = input("Please enter the ID: ")
    quantity = int(input("Please enter the quantity: "))
    record = SaleData(ID=ID, quantity=quantity)
    if Enqueue(record) == -1:
        return "Full"
    return "Stored"


print(EnterRecord())
print(EnterRecord())
print(EnterRecord())
print(EnterRecord())
print(EnterRecord())
print(EnterRecord())

print("")

result = Dequeue()
if result.quantity == -1:
    print("Error --> queue is empty")
print(f"Dequeued: ID: {result.ID} Quantity: {result.quantity} \n")

print(EnterRecord())

for item in CircularQueue:
    print(f"ID: {item.ID} Quantity: {item.quantity}")
