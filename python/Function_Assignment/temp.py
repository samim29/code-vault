#2nd method
def pushZeros(l):
  n=len(l)
  temp=[0]*n
  count=0
  for i in range(n):
    if l[i]!=0:
      temp[count]=l[i]
      count+=1
  while (count < n):
    temp[count]=0
  for i in range (n):
    l[i]=temp[i]
  return l

l=[0,0,2,0,7,0,4]
print(pushZeros(l))