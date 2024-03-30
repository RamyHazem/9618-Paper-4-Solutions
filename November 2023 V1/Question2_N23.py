# Even though this is the answer for part (c), it's best practice to declare all classes at the top of the file.
class RecordData(object):
    def __init__(self, ID, Total):
        """
        init the class
        :param ID: STRING
        :param Total: INTEGER
        """
        self.ID = ID
        self.Total = Total


Queue = ["" for i in range(50)]
HeadPointer = -1
TailPointer = 0


def Enqueue(string):
    global TailPointer
    global HeadPointer

    if TailPointer == 50:
        print("Queue is full")
        return

    if HeadPointer == -1:
        HeadPointer = 0

    Queue[TailPointer] = string
    TailPointer += 1


def Dequeue():
    global TailPointer
    global HeadPointer

    if TailPointer == HeadPointer or HeadPointer == -1:
        print("The Queue is empty")
        return "Empty"

    item = Queue[HeadPointer]
    HeadPointer += 1
    return item


def ReadData():
    try:
        with open("./QueueData.txt") as file:
            for line in file:
                Enqueue(line.strip())

    except Exception as e:
        print(f"Error: {e}")

    finally:
        file.close()


Records = []
NumberRecords = 0


def TotalData():
    global NumberRecords

    DataAccessed = Dequeue()
    if NumberRecords == 0:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords += 1
        return

    for i in range(0, NumberRecords):
        if Records[i].ID == DataAccessed:
            Records[i].Total += 1
            return

    Records.append(RecordData(DataAccessed, 1))
    NumberRecords += 1


def OutputRecords():
    for record in Records:
        print(f"ID: {record.ID} Total: {record.Total}")


ReadData()
for item in Queue:
    if item != "":
        TotalData()
OutputRecords()
