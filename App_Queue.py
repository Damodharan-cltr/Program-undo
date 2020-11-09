Queue =[]
def Enqueue(element):
    Queue.append(element)
    l = len(Queue)
    if l == 1:
        print(Queue[0])
    elif l == 2:
        print(Queue[1],Queue[0])
        
    else:
        for s in range(len(Queue)-1,-1,-1):
            print(Queue[s],end = " ")
        
def Dequeue():
    try:
        Queue.pop(0)
    except IndexError:
        print(-1)
    l = len(Queue)
    if l == 1:
        print(Queue[0])
    elif l == 2:
        print(Queue[1],Queue[0])
        
    else:
        for s in range(len(Queue)-1,-1,-1):
            print(Queue[s])

element = input("Enter A for Enqueue and D for Dequeue.")
if element.upper()=='A':
    print("Enter the element to Enqueue.")
    ele = int(input())
    Enqueue(ele)
else:
    Dequeue()
print("E for Exit or else C for continue")
com = input()
while com.upper() != "E":
    element = input("Enter A for Enqueue and D for Dequeue.")
    if element.upper()=='A':
        print("Enter the element to Enqueue.")
        ele = int(input())
        Enqueue(ele)
        print("\nE for Exit or else C for continue")
        com = input()
    else:
        Dequeue()
        print("\nE for Exit or else C for continue")
        com = input()
    





