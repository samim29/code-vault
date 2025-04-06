fruits =["apple","mango","cherry","banana"]#creating a list

print(fruits)#printing list

print(type(fruits))#check type of fruits

print(len(fruits))#check length of list

#checking if an item is present in the list
if "banana" in fruits:
    print("banana is present in list")
if "kiwi" not in fruits:
    print("kiwi is not in fruits")

#indexing in list
print(fruits[1])#mango
print(fruits[-2])#cherry, negative indexing  -1 refers to the last item, -2 refers to the second last item etc.

print(fruits[1:3])#['mango','cherry']
print(fruits[-3:-1])#['mango','cherry']

#adding elements in list
fruits.append("kiwi")
print(fruits)

fruits.insert(2,"lichi") #inserting at index
print(fruits)

more_fruits=["jackfruit","watermalon"]
fruits.extend(more_fruits)#concatinate two list
print(fruits)

#removing item from list
fruits.remove("watermalon")#remove specified item
print(fruits)

fruits.pop(4)#remove indexd item
print(fruits) 
fruits.pop()#remove last item
print(fruits)

#changing item in a list
fruits[1]="Pineapple" #change at index
print(fruits)

fruits[2:4]=["Blueberry","Strawberry"]
print(fruits)

#sorting a list
fruits.sort()#acending way
print(fruits)

fruits.sort(reverse=True)
print(fruits)#decending way

fruits.reverse()
print(fruits) #reversing


