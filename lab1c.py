def search(lst, key, index=0):
    if index >= len(lst):
        return -1   # not found
    if lst[index] == key:
        return index   # return position
    return search(lst, key, index + 1)

employees = [101, 102, 103, 104, 105]
key = int(input("Enter Employee ID to search: "))

pos = search(employees, key)
if pos != -1:
    print(f"Employee ID found at position {pos}")
else:
    print("Employee ID Not Found")
