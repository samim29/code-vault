#open the file in the read mode 
# file=open("python/fileHandling/file.txt","r")

#using file i can read

#through loop

# for line in file:
#     print(line)

#2nd method to read file
#print(file.read())

#using with statement

# with open ("python/fileHandling/file.txt","r") as file:
#     # data= file.read()
#     # print(data)
#     print(file.read(5)) #only read first 5 charecter 


# file=open("python/fileHandling/file2.txt","w")
# file.write("Hello world again")
# file.write("first my dtudents")
# file.close()

#same thing we can do with 'with' key word. here we dont need to explicitly close file
with open("python/fileHandling/file3.txt","w") as file:
    file.write("Hello world")

#for deleting module

# import os
# os. remove("python/fileHandling/file3.txt")