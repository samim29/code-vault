#creating set

#names={"Sia","Mia","Tia"}

#print set
#print(names)
#print(len(names))
#print(type(names))

#accessing item 
#for x in names:
   # print(x)
#checking if a item is in set
#if "Sia" in names:
   # print("sia is in the set")

#add elements in set
#names.add("ria")
#print(names)

#add anothe sequence in set
#name_list=["ria","kia","pia"]
#names.update(name_list)
#print(names)

#remove
#names.remove("Tia")
#print(names)

#names.discard("Ria") #this function will not throw an error if value is not present in set
#print(names)

#joining two sets
s1={'a','b','c'}
s2={'d','a','f'}
print(s1,s2)
#s3=s1.union(s2)
#print(s3)
#s1.update(s2)
#print(s1)

#keep only duplicates while joining
#s1.intersection_update(s2)
#print(s1)
s1.symmetric_difference_update(s2)
print(s1)

