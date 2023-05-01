def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Choosing the pivot
    pivot = arr[len(arr) // 2]

    # Partitioning the array
    smaller = []
    equal = []
    larger = []

    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)

    # Recursively sort the subarrays
    return quick_sort(smaller) + equal + quick_sort(larger)


# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = quick_sort(numbers)
print("Sorted array:", sorted_numbers)
