names = [
    "Alice",
    "Betty",
    "Cath",
    "Dean",
    "Emery",
    "Farmo",
    "Gregory",
    "Henry",
    "Houston"
]

def linear_search(array, value): # Looks at EVERY item one by one
    for name in array:
        if name == value:
            return True
    return False

def binary_search(array, value): # starts at the middle and decides where to go from there
    start = 0
    end = len(array) - 1

    found = False

    while not found and start <= end: 
        middle = (start + end) // 2

        # if found break
        if array[middle] == value:
            found == True
        else:
            if value < array[middle]:
                # search lower half
                end = middle - 1
            else: 
                # search upper half
                start = middle + 1
        return found


print(linear_search(names, "Henry"))
print(linear_search(names, "Jin"))

print(binary_search(names, "Cath"))
print(binary_search(names, "Jin"))
