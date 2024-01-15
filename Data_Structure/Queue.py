#Creating a non looping Queue
Queue = ["","","","",""]

#Setting variables
front = 0
rear = -1
size = 0

#creating subroutines
def enqueue(name):
    global size, rear
    if size != 5:
        rear = rear + 1 
        Queue[rear] = name
        size = size + 1
    elif size == 5:
        print("List if full!")

def dequeue():
    global size, front
    if size != 0:
        front = front + 1
        size = size -1
    if size == 0:
        print("list is empty!")

def showlist():
    for i in range(size):
        print(Queue[i + front])

#test program

dequeue()
enqueue("b")
enqueue("c")
enqueue("d")
enqueue("e")
dequeue()
showlist()
