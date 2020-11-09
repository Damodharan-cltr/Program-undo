ls =[]
def Insert(Element):
    ls.append(Element)
    print(ls)

def Remove(Element):
    ls.remove(Element)
    print(ls)

element = input("Enter I for Inser and R for Remove.")
if element.upper()=='I':
    print("Enter the element to Insert")
    ele = int(input())
    Insert(ele)
else:
    print("Enter the element to Remove")
    ele = int(input())
    Remove(ele)
print("E for Exit or else C for continue")
com = input()
while com.upper() != "E":
    element = input("Enter I for Insert and R for Remove.")
    if element.upper()=='I':
        print("Enter the element to Insert.")
        ele = int(input())
        Insert(ele)
        print("E for Exit or else C for continue")
        com = input()
    else:
        print("Enter the element to Remove")
        ele = int(input())
        Remove(ele)
        print("E for Exit or else C for continue")
        com = input()
    
