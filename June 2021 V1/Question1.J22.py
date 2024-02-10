class Node(object):
    def __init__(self, data, nextNode):
        """
        :param data: int
        :param nextNode: int
        """
        self.data = data
        self.nextNode = nextNode


linkedList = [Node(1, 1), Node(5, 4), Node(6, 7), Node(7, -1), Node(2, 2), Node(0, 6), Node(0, 8), Node(56, 3),
              Node(0, 9), Node(0, -1)]
startPointer = 0
emptyList = 5


def outputNodes(array, currentPointer):
    """
    output data from the linked list but following the nextNode values
    :param array: Node[]
    :param currentPointer: int
    :return: None
    """

    while currentPointer != -1:
        print(array[currentPointer].data)
        currentPointer = array[currentPointer].nextNode


# outputNodes(linkedList, startPointer)

def addNode(array, currentPointer, emptyList):
    """
    takes data as input from the user to be added to the end of the linked list in the next available space and
    update the relevant pointers
    :param array: Node[]
    :param currentPointer: int
    :param emptyList: int
    :return: bool
    """

    while True:
        user_data = input("Please enter the data: ")
        if user_data.isdigit():
            user_data = int(user_data)
            break
        print("Data entered is not valid.")

    if emptyList < 0 or emptyList > 9:
        print("No Empty Nodes! ")
        return False

    for node in array:
        if node.nextNode == -1:
            node.nextNode = emptyList
            break

    array[emptyList].data = user_data
    array[emptyList].nextNode = -1

    emptyList = array[emptyList].nextNode
    return True

# addNode(linkedList, startPointer, emptyList)


print("Before Adding Node: ")
outputNodes(linkedList, startPointer)
print("")
if addNode(linkedList, startPointer, emptyList):
    print("Value added to the linked list! ")
print("")
print("After Adding The Node: ")
outputNodes(linkedList, startPointer)
