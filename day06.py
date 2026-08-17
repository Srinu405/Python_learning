# LIST OPERATIONS

# CREATE A LIST WITH 3 ELEMENTS

a = [10, 20, 30]
print("Original list:", a)


# INSERT OPERATIONS



# APPENDING
# Add 5 types of non-sequence elements using append

a = [10, 20, 30]

a.append(40)          # int
a.append(10.5)        # float
a.append(2 + 3j)     # complex
a.append(True)        # bool
a.append(None)        # NoneType

print("\nAfter appending non-sequence elements:")
print(a)


# Add 5 types of sequence elements using append

a.append("Python")          # string
a.append([1, 2, 3])        # list
a.append((4, 5, 6))        # tuple
a.append({7, 8, 9})        # set
a.append({"a": 1})         # dictionary

print("\nAfter appending sequence elements:")
print(a)

# EXTENDING

# Add 5 types of non-sequence elements using extend

a = [10, 20, 30]

# extend requires an iterable
# So single non-sequence values are placed inside
# suitable iterable containers.

a.extend([40])             # int
a.extend([10.5])           # float
a.extend([2 + 3j])         # complex
a.extend([True])           # bool
a.extend([None])           # NoneType

print("\nAfter extending non-sequence elements:")
print(a)


# Add 5 types of sequence elements using extend

a.extend("Python")         # string
a.extend([1, 2, 3])        # list
a.extend((4, 5, 6))        # tuple
a.extend({7, 8, 9})        # set
a.extend({"a": 1, "b": 2}) # dictionary

print("\nAfter extending sequence elements:")
print(a)


# INSERTING

a = [10, 20, 30]

# Insert at index 1
a.insert(1, 100)
print("\nInsert at index 1:")
print(a)


# Insert at index -1
a.insert(-1, 200)
print("\nInsert at index -1:")
print(a)


# Insert at index 10000
a.insert(10000, 300)
print("\nInsert at index 10000:")
print(a)


# Insert at index -10000
a.insert(-10000, 400)
print("\nInsert at index -10000:")
print(a)



# DELETE OPERATIONS

# Create a list
a = [1, 2, 1, 3, 4, 1]

# Pop element at index 3
element = a.pop(3)

print("\nPopped element at index 3:")
print("Element:", element)
print("List:", a)


# Pop last element
element = a.pop()

print("\nPopped last element:")
print("Element:", element)
print("List:", a)


# Remove first 1
a.remove(1)

print("\nAfter removing first 1:")
print(a)


# Clear all elements
a.clear()

print("\nAfter clear:")
print(a)



# UPDATE OPERATIONS


# Sort ascending

a = [3, 2, 1, 5, 4]

a.sort()

print("\nAscending order:")
print(a)


# Sort descending

a = [3, 2, 1, 5, 4]

a.sort(reverse=True)

print("\nDescending order:")
print(a)


# Reverse the list

a = [3, 2, 1, 5, 4]

a.reverse()

print("\nReverse:")
print(a)



# READ OPERATIONS



a = [1, 2, 1, 3, 1, 2]

# Count of 1 and 2

print("\nCount of 1:", a.count(1))
print("Count of 2:", a.count(2))


# Index of 1 from start

print("Index of 1 from start:", a.index(1))


# Index of 1 from 2nd index

print("Index of 1 from 2nd index:", a.index(1, 2))


# Index of 1 from 5th index

print(a.index(1))                                 #ValueError


# TUPLE OPERATIONS



t = (1, 2, 1, 3, 1, 2)

# Count of 1 and 2

print("\nTuple count of 1:", t.count(1))
print("Tuple count of 2:", t.count(2))


# Index of 1 from start

print("Tuple index of 1 from start:", t.index(1))


# Index of 1 from 2nd index

print("Tuple index of 1 from 2nd index:", t.index(1, 2))


# Index of 1 from 5th index

try:                                                                                #ValueError
    print("Tuple index of 1 from 5th index:", t.index(1, 5))
except ValueError:
    print("1 is not present after index 5")