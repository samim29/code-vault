# write a function programme that takes a dictionary input and returns a new dictionary with the keys and values swapped.
def dict_swap(dict):
    new_dict={}
    for key,value in dict.items():
        if value in new_dict:
            new_dict[value].append(key)
        else:
            new_dict[value]=[key]
    return new_dict
dict={}
n=int(input("enter the number of key value pair in the dictionary"))
for i in range (n):
    key=input("Enter Key: ")
    value=input("Enter Value: ")
    dict[key]=value
print("Before Swapping Dictionary:",dict.items())
print("After Swapping Dictionary:",dict_swap(dict).items())
