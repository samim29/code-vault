def convertString(str):
    # Write your code here
    l=str.split()
    l2=[]
    for i in l:
        x=i.capitalize()
        l2.append(x)
    
    print(" ".join(l2))
    

str="I am a student of the third year"
convertString(str)