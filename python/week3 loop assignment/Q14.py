'''14. Given three numbers A, B and C, write a program to write their values in an ascending order. For example, 
if A=12, B=10, and C=15,

your program should print out:

Smallest number = 10

Next higher number = 12 Highest number = 15

Note Don't use any python inbuilt function, Use only Loop'''

   
A=int(input("ENter the value of A"))
B=int(input("ENter the value of B"))
C=int(input("ENter the value of C"))
# Assume A is the smallest number
smallest = A
next_higher = A
highest=A

#find smallest
if B<smallest:
    smallest=B
if C<smallest:
    smallest=C

#finding highest
if B>highest:
    highest=B
if C>highest:
    highest=C

#finding next highest
if A!=smallest and A!=highest:
    next_higher=A
elif B!=smallest and B!=highest:
    next_higher=B
else:
    next_higher=C



# Print the sorted numbers
print("Smallest number =", smallest)
print("Next higher number =", next_higher)
print("Highest number =", highest)