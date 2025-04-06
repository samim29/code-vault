# (b)

# 0

# 2 2

# 4 4 4

# 8 8 8 8

rows = 4  # Number of rows in the pattern

# Loop through each row
for i in range(rows):
    for j in range(i + 1):
        if i==0:
            print('0',end=" ")
        else:    
            print(2 ** i, end=" ")
    print()  # Move to the next line for the next row

