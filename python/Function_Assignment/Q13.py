'''Write a Python function that takes a variable number of arguments and returns a new string that is the 
concatenation of all the arguments'''
def return_string(*args):
    result=""
    for arguments in args:
        result+=str(arguments)  #you can use join() function . go and google about it
        
    return result
    

print(return_string(1,2,3,4,5,"hi",3.4))