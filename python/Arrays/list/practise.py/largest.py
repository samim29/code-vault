# Taking the input for the first list
l1 = []
n = int(input("Enter the number of elements in the first list: "))
for i in range(n):
    a = int(input())
    l1.append(a)
print("List 1:", l1)

# Taking the input for the second list
l2 = []
m = int(input("Enter the number of elements in the second list: "))
for i in range(m):
    b = int(input())
    l2.append(b)
print("List 2:", l2)

# Initialize the resulting list
l = []

# Sum elements based on the smaller list size
if n == m:
    for i in range(n):
        sum_value = l1[i] + l2[i]  # Ensure both lists have elements at index i
        l.append(sum_value)
elif n > m:
    for i in range(m):  # Only iterate through the smaller list length
        sum_value = l1[i] + l2[i]
        l.append(sum_value)
    
    # Append remaining elements from the longer list (l1)
    for i in range(m, n):
        l.append(l1[i])
else :
    for i in range(n):  # Only iterate through the smaller list length
        sum_value = l1[i] + l2[i]
        l.append(sum_value)
    
    # Append remaining elements from the longer list (l2)
    for i in range(n, m):
        l.append(l2[i])

# Print the resulting list
print("Resulting list:", l)



