#ceate a looping queue
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
        if rear == 5:
            rear = rear - 5
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
        x= i + front
        if x == 5:
            x=x-5
        print(Queue[i + front])

#Testing

enqueue("a")
enqueue("b")
enqueue("c")
enqueue("d")
enqueue("e")
enqueue("f")
enqueue("g")
enqueue("h")
showlist()