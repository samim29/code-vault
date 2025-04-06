#wap for swapping two elements in a list
l=[10,11,12,13,14]
print(l)
indx1=int(input("enter the first index: "))
indx2=int(input("enter the second index: "))
#first method
temp=l[indx1]
l[indx1]=l[indx2]
l[indx2]=temp
print(l)
#2nd method
l[indx1]=l[indx1]+l[indx2]
l[indx2]=l[indx1]-l[indx2]
l[indx1]=l[indx1]-l[indx2]
print(l)


