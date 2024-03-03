Jobs = []
global NumberOfJobs


def Initialise():
    global NumberOfJobs
    for i in range(100):
        Jobs.append([-1, -1])
    NumberOfJobs = 0

    return Jobs, NumberOfJobs


def AddJob(num, priority):
    global Jobs
    for i in range(0, len(Jobs)):
        if Jobs[i][0] == -1:
            Jobs[i] = [num, priority]
            return "Added"

    return "Not added"

Initialise()
print(AddJob(12, 10))
print(AddJob(526, 9))
print(AddJob(33, 8))
print(AddJob(12, 9))
print(AddJob(78, 1))

def InsertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1][1] > arr[j][1] and j > 0:
            arr[j - 1], arr[j] = arr[j - 1], arr[j]
            j -= 1

    return arr


def PrintArr():
    global Jobs
    for job in Jobs:
        if job[0] != -1:
            print(f"{job[0]} priority {job[1]}")

InsertionSort(Jobs)
PrintArr()