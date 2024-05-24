class Box:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(curr):
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
def insertAtTailNode(head, ele):
    temp = Box(ele) 
    if head == None:
        return temp
    tail = head 
 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp
    return head 
 
def insertAtBeginning(head, ele):
    temp = Box(ele)
    if head == None:
        return temp 
    temp.next = head 
    return temp
 
def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtBeginning(head, ele)
 
    temp = Box(ele)
    currentIndex = 0 
    currentNode = head 
    while currentIndex != position - 1:
        currentIndex += 1 
        currentNode = currentNode.next 
 
    temp.next = currentNode.next 
    currentNode.next = temp 
    return head
 
 
def deleteHeadNodeInLinkedList(head):
    if head == None:
	    return None 
    secondNode = head.next 
    head.next = None 
    return secondNode 
 
def deleteNodeAtSpecificPosition(head, position):
    if position == 0:
        return deleteHeadNodeInLinkedList(head)
 
    currentIndex = 0 
    currentNode = head 
    while currentIndex != position - 1:
        currentIndex += 1 
        currentNode = currentNode.next 
 
    nodeToBeDeleted = currentNode.next 
    currentNode.next = nodeToBeDeleted.next 
    nodeToBeDeleted.next = None 
    return head
 
 
head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head = insertAtBeginning(head, ele)
 
printLinkedList(head)
head = deleteNodeAtSpecificPosition(head, 5)
printLinkedList(head)