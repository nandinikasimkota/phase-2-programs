#Array based imp of Stack
def push(stack, ele):
    stack.insert(0, ele)
    print(ele, " inserted into stack successfully")
 
def pop(stack):
    if len(stack) == 0:
        print("stack is empty")
        return 
    print(stack[0], "deleted successfully")
    stack.pop(0)
 
stack = []
push(stack, 10)
push(stack, 20)
push(stack, 30)
push(stack, 40)
push(stack, 50)
 
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)