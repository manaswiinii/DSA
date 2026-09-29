def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid   # found
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1   # not found


n = int(input("Enter no. of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Check if already sorted
if arr == sorted(arr):
    print("\nThe input list is already sorted.")
else:
    print("\nThe input list is not sorted.")
    print("Sorting the list...")
    arr.sort()

print("Sorted list:", arr)

key = int(input("Enter element to search: "))
result = binary_search(arr, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found.")
