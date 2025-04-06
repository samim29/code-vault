 #Write a Python program to multiply all the items in a list.
def multiply(l):
    result=1
    for i in l:
        result=i*result
    return result
n=int(input("enter the size of list:"))
l=[]
print("enter the items: ")
for i in range(n):
    l.append(int(input()))
print("the result of multiplication is: ", multiply(l))