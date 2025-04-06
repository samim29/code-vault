#creating tuple
colours=("red","yellow","green")
#2n method
fruits=tuple(("apple","banana"))

#creating a tuple with 1 item
fruit=("apple",)#if don't put comma then it will consider as string
#fruit=tuple(("apple")) 2nd method

#check type of tuple
print(type(fruit))

#check length of tuple
print(len(colours))

#accessing tuple

print(colours[1])#yellow
print(colours[-1])#green negative indexing
print(colours[1:3])#range indexing ("yellow", "green")
print(colours[-3:-1]) #negative range index

#check if a item is in tuple
if "green" in colours:
    print("green is present in colours")

#traverse the tuple
for i in colours:
    print(i)

#concatinate two tuple
more_colours=("blue","brown")
colours=colours + more_colours
print(colours)

#unpacking a tuple
colour1, colour2 =colours
print(colour1)