#  Big O Notation
#  Relationship between an input and the output

def foo(n):                           # This is O(n)
    for i in range(0, n):             # O(n)
        print(i)                      # O(1)
        new_num = i * 100             # O(1)
        print(new_num)                # O(1)

def bar(n):                           # This is O(n^2)
    s = 0                             # O(1)
    for i in range(n):                # O(n)
        for j in range(n):            # O(n)
            s += i * j                # O(1) (constant time because n doesn't change anything)
    return s                          #


def baz(n):                           # This is 
    s = 0                             # O(1)
    for i in range(n):                # O(n)
        for j in range(int(sqrt(n))): # O(n)
            s += i * j                #  O(1)
    return s                          # 