def bubble_sort_swaps(arr, ascending=True):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
    return count

# Main function to handle input and output
def best_bubble_sort():
    # Input reading
    n = int(input())  # Number of elements
    arr = list(map(int, input().split()))  # Array of elements
    
    # Copy the array to sort in both directions
    ascending_arr = arr.copy()
    descending_arr = arr.copy()
    
    # Get swap counts for ascending and descending
    asc_swaps = bubble_sort_swaps(ascending_arr, ascending=True)
    desc_swaps = bubble_sort_swaps(descending_arr, ascending=False)
    
    # Return the minimum of the two swap counts
    print(min(asc_swaps, desc_swaps))

# Calling the main function to execute the solution
best_bubble_sort()
