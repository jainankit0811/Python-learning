# Creating an empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)  # Adding the element
b.add(5)
# b.add([4, 5, 6])  # We can't add list element [4,5,6]
b.add((4, 5, 6))  # We adding the tuples
# b.add({4: 5}) # We can't add list element {4,5,6}
print(b)

print(len(b))  # prints the length of this set

b.remove(5)  # Remove 5 fromt set b
# b.remove(15) # throws an error while trying to remove 15(which is not present in the set)

print(b)

print(b.pop())  # It is removes any element in set
print(b.clear())  # It making empty set b
