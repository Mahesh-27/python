def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target value not found

# Example usage:
array = [2, 4, 6, 8, 10, 12, 14, 16]
target_value = 3

result = binary_search(array, target_value)

if result != -1:
    print("Target value found at index", result)
else:
    print("Target value not found in the array.")
