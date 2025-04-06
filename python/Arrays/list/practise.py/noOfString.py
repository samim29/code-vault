# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def noOfString(l):
    ctr=0
    for i in l:
        if len(i)>1 and i[0]==i[-1] :
            ctr+=1
    return ctr

l=[]
n=int(input("size of list: "))
for i in range(n):
    l.append(input("enter list element: "))
print("total no of string having first and last charecter is same is : ", noOfString(l))
