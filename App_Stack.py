Stack =[]
def Push(element):
    Stack.append(element)
    l = len(Stack)
    if l == 1:
        print(Stack[0])
    elif l == 2:
        print(Stack[1])
        print(Stack[0])
        
    else:
        for s in range(len(Stack)-1,-1,-1):
            print(Stack[s])
        
def Pop():
    try:
        Stack.pop()
    except IndexError:
        print(-1)
    l = len(Stack)
    if l == 1:
        print(Stack[0])
    elif l == 2:
        print(Stack[1])
        print(Stack[0])
        
    else:
        for s in range(len(Stack)-1,-1,-1):
            print(Stack[s])

element = input("Enter A for push and P for pop.")
if element.upper()=='A':
    print("Enter the element to push.")
    ele = int(input())
    Push(ele)
else:
    Pop()
print("E for Exit or else C for continue")
com = input()
while com.upper() != "E":
    element = input("Enter A for push and P for pop.")
    if element.upper()=='A':
        print("Enter the element to push.")
        ele = int(input())
        Push(ele)
        print("E for Exit or else C for continue")
        com = input()
    else:
        Pop()
        print("E for Exit or else C for continue")
        com = input()
    





