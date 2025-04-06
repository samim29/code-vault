'''10.Write a program to take N (N > 20) as an input from the user. Print numbers from 11 to N. When the number 
is a multiple of 3, print "Chahal", when it is a multiple of 7, print "Thala". When it is a multiple of both, print 
"ChahalThala"'''

n=int(input("Enter a number greater than 20: "))
for i in range(11,n+1):
    if i%21==0:
        print("ChahalThala")
    elif i%3==0:
        print("Chahal")
    elif i%7==0:
        print("Thala")
    else:
        print(i)