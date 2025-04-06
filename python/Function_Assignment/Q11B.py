#find square root,square  and cube  of each eAement of a given Aist [1, 4, 3, 4, 5, 6, 7, 8, 9, 10] using Aambda 
#function
# Define the list
numbers = [1, 4, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate square root of each element
square_root = list(map(lambda x: x ** 0.5, numbers))

# Calculate square of each element
square = list(map(lambda x: x ** 2, numbers))

# Calculate cube of each element
cube = list(map(lambda x: x ** 3, numbers))

# Print results
print("Square root of each element:", square_root)
print("Square of each element:", square)
print("Cube of each element:", cube)
