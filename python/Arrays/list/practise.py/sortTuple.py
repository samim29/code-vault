# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
def sort_Tuple_in_list(l,n):
    for i in range (n) :
        for i in l:
            if i[1]>i+1[1]:
                temp=i
                i=i+1
                i+1 =temp
    return l



l=[]
n=int(input("size of list: "))
l1=sort_Tuple_in_list(l)
print(l1)
