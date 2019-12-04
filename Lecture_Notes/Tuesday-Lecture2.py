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

def linear_search(array, value):
    for name in array:
        if name == value:
            return True
    return False

def binary_search(array, value):
    pass


print(linear_search(names, "Henry"))
print(linear_search(names, "Jin"))
