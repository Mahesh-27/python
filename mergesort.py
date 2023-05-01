def merge_sort(a):
    if len(a) > 1:
        left_arr = a[:len(a)//2]
        right_arr = a[len(a)//2:]

        # Recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge and sort
        i = 0   # Left arr index
        j = 0   # Right arr index
        k = 0   # Merged arr index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                a[k] = left_arr[i]
                i += 1
            else:
                a[k] = right_arr[j]
                j += 1
            k += 1

        # Append remaining elements from left or right sublist
        while i < len(left_arr):
            a[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            a[k] = right_arr[j]
            j += 1
            k += 1

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
merge_sort(numbers)
print("Sorted array:", numbers)
