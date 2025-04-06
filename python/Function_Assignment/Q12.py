#c).Write a Python function that takes any number of keyword arguments and prints the keys and values of 
#the arguments

def greet(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


greet(name="Alice",greeting="Hello")