class Box:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printStack(curr):
    if curr == None:
        print("Stack is empty")
        return 
 
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
def pop(head):
    if head == None:
	    return None 
	print(head.data, " deleted successfully")
    secondNode = head.next 
    head.next = None 
    return secondNode 
 
def push(head, ele):
    print(ele, " inserted successfully")
    temp = Box(ele)
    if head == None:
        return temp 
    temp.next = head 
    return temp
 
head = None 
head = push(head, 10)
head = push(head, 20)
head = push(head, 30)
head = push(head, 40)
printStack(head)
 
head = pop(head)
printStack(head)
 
head = pop(head)
printStack(head)
 
head = pop(head)
printStack(head)
 
head = pop(head)
printStack(head)
 
head = pop(head)
printStack(head)
