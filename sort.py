def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track whether any swaps happen in this pass
        swapped = False

        # Last i elements are already sorted, so the inner loop can avoid looking at them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, then the array is already sorted
        if not swapped:
            break

    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array is:", sorted_arr)
