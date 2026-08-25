def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i   # return index if found
    return -1   # return -1 if not found

n = int(input("Enter no. of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter element to search: "))
result = linear_search(arr, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found.")
