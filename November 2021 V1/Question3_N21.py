ArrayNodes = [[0, 0, 0] for i in range(20)]
RootPointer = -1
FreeNode = 0

def AddNode(array, rootPointer, freeNodePointer):
    global RootPointer  # Declare RootPointer as a global variable
    NodeData = int(input("Enter the data: "))
    if freeNodePointer <= 19:
        array[freeNodePointer][0] = -1
        array[freeNodePointer][1] = NodeData
        array[freeNodePointer][2] = -1
        if rootPointer == -1:
            RootPointer = 0  # Update the global RootPointer
        else:
            placed = False
            currentNode = rootPointer
            while not placed:
                if NodeData < array[currentNode][1]:
                    if array[currentNode][0] == -1:
                        array[currentNode][0] = freeNodePointer
                        placed = True
                    else:
                        currentNode = array[currentNode][0]
                else:
                    if array[currentNode][2] == -1:
                        array[currentNode][2] = freeNodePointer
                        placed = True
                    else:
                        currentNode = array[currentNode][2]
        freeNodePointer += 1
    else:
        print("Tree is full")
    return RootPointer  # Return the updated rootPointer

def PrintAll():
    for i in range(len(ArrayNodes)):
        print(f"{ArrayNodes[i][0]} {ArrayNodes[i][1]} {ArrayNodes[i][2]}")

for i in range(10):
    RootPointer = AddNode(ArrayNodes, RootPointer, FreeNode)

PrintAll()
