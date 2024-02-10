StackData = [] # 1 to 10 Items
StackPointer = 0

def output_array_data(array):
    print(StackPointer)
    for item in array:
        print(item)

def Push(integer):
    global StackPointer
    if len(StackData) == 10:
        return False

    StackData.append(integer)
    StackPointer += 1
    return True

def Pop():
    global StackPointer
    if len(StackData) == 0:
        return -1
    StackData.pop()
    StackPointer -= 1


for num in range(0, 11):
    new_num = input("Enter a number to add to the stack: ")
    result = Push(new_num)
    if result:
        print("Number added to stack")
    else:
        print("Stack is Full")

Pop()
Pop()

output_array_data(StackData)


