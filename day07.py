#SET METHODS
#create a empty dict and print its type
d ={}
print(type(d))
#create a empty set and print its type
s=set()
print(type(s))
#add 5 non-sequences and 6 sequences to that set with add method
s.add(5)
s.add(3.4)
s.add(True)
s.add((3+5j))
s.add(None)
s.add('abc')
s.add("Python")       
s.add((1, 2, 3))      
s.add(range(5))          
print(s)
#add 5 non-sequences and 6 sequences with update method
s.update([10])         
s.update([10.5])       
s.update([2 + 3j])     
s.update([True])       
s.update([None]) 
s.update("Python")
s.update((1, 2, 3))
s.update([4, 5, 6])
s.update({7, 8, 9})
s.update(range(3))
print(s)
#print a set and remove first element from that set
s = {10, 20, 30, 40, 50}
print(s)
element = s.pop()
print(element)
print(s)
#remove one existing and one non-existing element from that set
s.remove(30)
print(s)
#discard one existing and one non-existing element from that set
s.discard(30)
print(s)
s.discard(100)
print(s)
#remove all elements from the set
s.clear()
#create a set {1,2,3,4}, a list [3,4,5,6]. 
#write union of set and list
#write intersection of set and list
#write difference of set and list
#write symmetric difference of set and list
#use union, intersection, difference, symmetric difference operators on set and another set. try to change second type of list and see outputs
a = {1, 2, 3, 4}
b = [3, 4, 5, 6]
print(a)
print(b)
# Union
print(a.union(b))
# Intersection
print(a.intersection(b))
# Difference
print(a.difference(b))
# Symmetric difference
print(a.symmetric_difference(b))
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a)
print(b)
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)


#DICT METHODS
#create a empty dict
d = {}
print(d)
#extend dict with another dict
d = {}
d.update({1: "a", 2: "b"})
print(d)
#extend dict with another list
d = {}
d.update([(1, "a"), (2, "b")])
print(d)     
#extend dict with another tuple
d = {}
d.update(((1, "a"), (2, "b")))
print(d)
#extend dict with another set
d = {}
d.update({(1, "a"), (2, "b")})
print(d)
#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
#remove the pair with key 4
#remove the pair with key 100
#remove the pair with key 100 if not there return 'z'
#remove the last pair
#remove all elements from the dict
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# Remove key 4
d.pop(4)
print(d)
# Remove key 100
# This causes KeyError if used directly
# d.pop(100)
# Remove key 100 and return 'z' if not present
result = d.pop(100, 'z')
print(result)
# Remove last pair
result = d.popitem()
print(result)
print(d)
# Remove all elements
d.clear()
print(d)
#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
#get the value of key 4
#get the value of key 100
#get the value of key 100, if key is not present get 'z'
print(d.get(4))
print(d.get(100))
print(d.get(100, 'z'))
#get the value of key 4 with setdefault
#get the value of key 100 with setdefault
#get the value of key 100 with setdefault, if key is not there add 100 with 'z'
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(d.setdefault(4))
print(d.setdefault(100))
print(d.setdefault(100, 'z'))
print(d)
#get all keys of dict and print its type
#get all values in dict and print its type
#get all items in dict and print its type
keys = d.keys()
print(keys)
print(type(keys))
values = d.values()
print(values)
print(type(values))
items = d.items()
print(items)
print(type(items))


