#ceate a looping queue
Queue = ["","","","",""]
print("working?_")
#Setting variables
front = 0
rear = -1
size = 0
full = 0
printer = 0

#creating subroutines
def enqueue(name):
    global size, rear, full
    if (size < 5) or (full == 5):
        rear = rear + 1 
        if rear == 5:
            rear = rear - 5
        Queue[rear] = name
        size = size + 1
    
    if size == 5:
       full = 5
    
    if full == 5:
        size = 5


def dequeue():
    global size, front
    if size != 0:
        front = front + 1
        size = size -1
    

def showlist():
    global size, front, printer
    printer = front
    if size == 0:
        print("there is no list")
    for i in range(size):
        print(Queue[printer])
        printer = printer + 1
        if printer == 5:
            printer = printer - 5


    

#Testing

enqueue("a")
enqueue("b")
enqueue("c")
enqueue("d")
enqueue("e")
dequeue()
showlist()
