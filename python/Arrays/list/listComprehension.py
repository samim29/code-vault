
# when we ment to make a new list from items of an existing list.

fruits=["apple","mango","cherry","banana","lemon"]
new_fruits=[fruit for fruit in fruits if "a" in fruit] #['apple', 'mango', 'banana']
print(new_fruits)

#copy a list
new_fruits=fruits.copy()#['apple', 'mango', 'cherry', 'banana', 'lemon']
print( new_fruits)

#concatinate two list
new_fruits=fruits+new_fruits#['apple', 'mango', 'cherry', 'banana', 'lemon', 'apple', 'mango', 'cherry', 'banana', 'lemon']
print( new_fruits)

#nested list

fruits=["apple","mango",["cherry","banana"],"lemon"]
print(fruits[2])#["cherry","banana"]
fruits.insert(3,["lichi","pumkin"])
print(fruits)#['apple', 'mango', ['cherry', 'banana'], ['lichi', 'pumkin'], 'lemon']
print(fruits[3][0])#lichi
