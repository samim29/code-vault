 # Write a Python program to sum all the items in a list
def mulOfItems(list):
    mul=1;
    for i in list:
     mul=mul*i
    return mul


l=[]
n=int(input("size of list: "))
for i in range(n):
    l.append(int(input("enter list element: ")))

mul=mulOfItems(l)

print("mul of the elements of list is: ",mul)
