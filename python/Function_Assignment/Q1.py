#
def List_Mean(list):
    sum=0
    for i in list:
        sum+=i
    mean=sum/len(list)
    return mean

n=int(input("Enter the size of list: "))
l=[]
for i in range(n):
    l.append(float(input()))
print("The mean of the elements in the list is",List_Mean(l))