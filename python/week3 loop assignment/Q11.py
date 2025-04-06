####  11. Write programs using nested loops
'''
A
A B
A B C D
A B C D E
A B C D E F'''

r=int(input("Enter the number of rows:"))
for i in range (r):
    ch=65
    for j in range(i+1):
        print(chr(ch+j),end=" ")
        
    print()