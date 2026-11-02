print("Manaswini-CSE25102")

size = 10
chain = [[] for _ in range(size)]
linear = [None] * size
quadratic = [None] * size

n = int(input("Enter number of elements: "))
keys = []

for i in range(n):
    keys.append(int(input("Enter value: ")))

# Separate Chaining
for key in keys:
    chain[key % size].append(key)

# Linear Probing
for key in keys:
    index = key % size
    count = 0

    while linear[index] is not None and count < size:
        index = (index + 1) % size
        count += 1

    if count == size:
        print("Cannot insert:", key)
    else:
        linear[index] = key

# Quadratic Probing
for key in keys:
    index = key % size
    i = 0

    while i < size and quadratic[(index + i * i) % size] is not None:
        i += 1

    if i == size:
        print("Cannot insert:", key)
    else:
        quadratic[(index + i * i) % size] = key

# Display Separate Chaining
print("\nSeparate Chaining:")
for i in range(size):
    print(i, ":", chain[i])

# Display Linear Probing
print("\nLinear Probing:")
for i in range(size):
    print(i, ":", linear[i])

# Display Quadratic Probing
print("\nQuadratic Probing:")
for i in range(size):
    print(i, ":", quadratic[i])
