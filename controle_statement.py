'''
controle statements in python
'''
# Example list
fruits = ["apple", "banana", "cherry"]

# Check if an item is in the list
item = "banana"
if item in fruits:
    print(f"{item} is in the list.")
else:
    print(f"{item} is not in the list.")
'''elif'''
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
'''for loop'''
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
'''while loop'''
count = 0

while count < 5:
    print(count)
    count += 1
'''break'''
for i in range(10):
    if i == 5:
        break
    print(i)
'''cotinue'''
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
