# Example demonstrating identity in Python

# Two identical lists with the same contents
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# Checking for equality (==)
print("list1 == list2:", list1 == list2)  # True

# Checking for identity (is)
print("list1 is list2:", list1 is list2)  # False, because they are different objects in memory

# Displaying their unique memory IDs
print("id(list1):", id(list1))
print("id(list2):", id(list2))

# Assigning the same object to another variable
list3 = list1

# Now list1 and list3 refer to the same object
print("list1 is list3:", list1 is list3)  # True, they are the same object
print("id(list3):", id(list3))  # Same as id(list1)