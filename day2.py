# ==========================================
# PYTHON DAY 3 - DATATYPES & TYPE CONVERSION
# ==========================================


# ------------------------------------------
# 1. DATA TYPES
# ------------------------------------------

# int
a = 10

# float
b = 10.5

# complex
c = 2 + 3j

# bool
d = True

# NoneType
e = None

# string
f = "Python"

# range
g = range(5)

# list
h = [1, 2, 3]

# tuple
i = (1, 2, 3)

# set
j = {1, 2, 3}

# dictionary
k = {"name": "Srinu", "age": 21}


# Print data types

print("DATA TYPES")

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))


# ------------------------------------------
# 2. TYPE CONVERSION
# ------------------------------------------




# int to float

a = 10
b = float(a)

print("int to float:")
print(b)
print(type(b))


# float to int

a = 10.5
b = int(a)


print(b)
print(type(b))


# int to string

a = 100
b = str(a)


print(b)
print(type(b))


# string to int

a = "100"
b = int(a)


print(b)
print(type(b))


# list to tuple

a = [1, 2, 3]
b = tuple(a)


print(b)
print(type(b))


# tuple to list

a = (1, 2, 3)
b = list(a)


print(b)
print(type(b))


# list to set

a = [1, 2, 3, 2, 1]
b = set(a)


print(b)
print(type(b))


# range to list

a = range(5)
b = list(a)


print(b)
print(type(b))