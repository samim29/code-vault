str=input("Enter your String ")
length=len(str)
l=[]
word=""
for i in range (0,length):
    if (str[i]==" "): #split the word in the position of " " and append it in to a list
        l.append(word)
        word=""
    else:
        word=word+str[i] #concatinate each charecter of the strng and make a word

if word: #for the last word
    l.append(word)

print(l) #print the list containing the words