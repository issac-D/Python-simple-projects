
# Variable Declaration in Python

In Python, variables are used to store data values. Unlike some other programming languages, Python does not require explicit declaration of variables, which means you don't need to specify the type of a variable before using it. The type of a variable is determined by the value assigned to it.

## Declaring Variables

To declare a variable in Python, you simply need to assign a value to it using the `=` operator:

```python
# Variable declaration
x = 5       # Integer variable
y = 3.14    # Float variable
name = "Alice"  # String variable
is_valid = True  # Boolean variable
```

In the example above:
- `x` is an integer variable.
- `y` is a float variable.
- `name` is a string variable.
- `is_valid` is a boolean variable.

## Dynamic Typing

Python is dynamically typed, meaning the type of a variable can change during execution:

```python
x = 5       # x is an integer
x = "Hello" # Now x is a string
```

## Variable Naming Rules

When naming variables in Python, follow these rules:
- Variable names must start with a letter (a-z, A-Z) or an underscore (_).
- The remaining characters can be letters, digits (0-9), or underscores.
- Variable names are case-sensitive (`age`, `Age`, and `AGE` are different variables).

Valid examples:
```python
my_var = 10
_myVar = "Hello"
myVar2 = 3.14
```

Invalid examples:
```python
2myVar = 10   # Starts with a digit
my-var = "Hello"  # Contains a hyphen
my var = 3.14  # Contains a space
```

## Constants

Although Python does not have built-in constant types, the convention is to use all uppercase letters to signify that a variable should not change:

```python
PI = 3.14159
MAX_USERS = 100
```

While Python doesn't enforce this, it's a good practice to follow.

## Conclusion

Declaring variables in Python is straightforward. Just assign a value to a name, and Python takes care of the rest. Remember to follow the naming rules and use uppercase letters for constants to keep your code readable and maintainable.



# Data Types in Python

Python has several built-in data types that allow you to work with different kinds of data. Here are the most common ones:

## Numeric Types

1. **Integers** (`int`): Whole numbers, positive or negative, without decimals.
   ```python
   age = 25        # Integer
   temperature = -5   # Negative integer
   ```
   
2. **Floating-Point Numbers** (`float`): Numbers that contain a decimal point.
   ```python
   height = 5.9    # Float
   price = 19.99   # Float
   ```
   
3. **Complex Numbers** (`complex`): Numbers with a real and an imaginary part.
   ```python
   z = 3 + 5j      # Complex number
   ```

## Sequence Types

1. **Strings** (`str`): A sequence of characters enclosed in single or double quotes.
   ```python
   name = "Alice"    # String
   greeting = 'Hello, World!'  # String
   ```
   
2. **Lists** (`list`): Ordered, mutable collections of items, which can be of different types.
   ```python
   fruits = ["apple", "banana", "cherry"]  # List of strings
   mixed_list = [1, "Hello", 3.14, True]    # List of different types
   ```
   
3. **Tuples** (`tuple`): Ordered, immutable collections of items, which can be of different types.
   ```python
   coordinates = (10.0, 20.0)    # Tuple of floats
   person = ("Alice", 25, "Engineer")  # Tuple of different types
   ```

4. **Ranges** (`range`): Immutable sequences of numbers, typically used in loops.
   ```python
   numbers = range(1, 10)   # Range from 1 to 9
   ```

## Mapping Types

1. **Dictionaries** (`dict`): Unordered collections of key-value pairs.
   ```python
   person = {"name": "Alice", "age": 25, "profession": "Engineer"}
   ```

## Set Types

1. **Sets** (`set`): Unordered collections of unique items.
   ```python
   fruit_set = {"apple", "banana", "cherry"}
   ```

2. **Frozen Sets** (`frozenset`): Immutable versions of sets.
   ```python
   frozen_fruit_set = frozenset(["apple", "banana", "cherry"])
   ```

## Boolean Type

1. **Booleans** (`bool`): Represents one of two values: `True` or `False`.
   ```python
   is_valid = True
   is_empty = False
   ```

## None Type

1. **NoneType** (`NoneType`): Represents the absence of a value.
   ```python
   result = None
   ```

## Type Conversion

Python allows you to convert between different data types using type conversion functions. Here are a few examples:

```python
# Convert float to int
x = 3.14
y = int(x)   # y will be 3

# Convert int to float
a = 5
b = float(a)  # b will be 5.0

# Convert int to string
age = 25
age_str = str(age)   # age_str will be '25'

# Convert string to int
number_str = "123"
number = int(number_str)  # number will be 123
```

## Conclusion

Understanding Python's data types is crucial for effective programming. Each data type serves a specific purpose, and choosing the right one can make your code more efficient and readable. Whether you're working with numbers, text, or collections of data, Python's rich set of data types has you covered.



# Operation Types in Python

Python provides a variety of operations that you can perform on data. These operations can be broadly categorized into several types:

## Arithmetic Operations

Arithmetic operations are used to perform mathematical calculations.

1. **Addition** (`+`)
   ```python
   x = 5 + 3  # x will be 8
   ```

2. **Subtraction** (`-`)
   ```python
   y = 10 - 4  # y will be 6
   ```

3. **Multiplication** (`*`)
   ```python
   z = 7 * 6  # z will be 42
   ```

4. **Division** (`/`)
   ```python
   a = 20 / 4  # a will be 5.0
   ```

5. **Floor Division** (`//`): Division that returns the largest integer less than or equal to the result
   ```python
   b = 20 // 3  # b will be 6
   ```

6. **Modulus** (`%`): Returns the remainder of a division
   ```python
   c = 20 % 3  # c will be 2
   ```

7. **Exponentiation** (`**`): Raises a number to the power of another number
   ```python
   d = 2 ** 3  # d will be 8
   ```

## Comparison Operations

Comparison operations are used to compare two values and return a boolean (`True` or `False`).

1. **Equal to** (`==`)
   ```python
   result = (5 == 5)  # result will be True
   ```

2. **Not equal to** (`!=`)
   ```python
   result = (5 != 3)  # result will be True
   ```

3. **Greater than** (`>`)
   ```python
   result = (10 > 5)  # result will be True
   ```

4. **Less than** (`<`)
   ```python
   result = (3 < 7)  # result will be True
   ```

5. **Greater than or equal to** (`>=`)
   ```python
   result = (5 >= 5)  # result will be True
   ```

6. **Less than or equal to** (`<=`)
   ```python
   result = (2 <= 4)  # result will be True
   ```

## Logical Operations

Logical operations are used to combine conditional statements.

1. **Logical AND** (`and`)
   ```python
   result = (5 > 3 and 10 > 5)  # result will be True
   ```

2. **Logical OR** (`or`)
   ```python
   result = (5 > 3 or 10 < 5)  # result will be True
   ```

3. **Logical NOT** (`not`)
   ```python
   result = not (5 > 3)  # result will be False
   ```

## Bitwise Operations

Bitwise operations work on binary representations of numbers.

1. **Bitwise AND** (`&`)
   ```python
   result = 5 & 3  # result will be 1 (0101 & 0011 = 0001)
   ```

2. **Bitwise OR** (`|`)
   ```python
   result = 5 | 3  # result will be 7 (0101 | 0011 = 0111)
   ```

3. **Bitwise XOR** (`^`)
   ```python
   result = 5 ^ 3  # result will be 6 (0101 ^ 0011 = 0110)
   ```

4. **Bitwise NOT** (`~`)
   ```python
   result = ~5  # result will be -6 (inverts all bits)
   ```

5. **Bitwise Left Shift** (`<<`)
   ```python
   result = 5 << 1  # result will be 10 (0101 << 1 = 1010)
   ```

6. **Bitwise Right Shift** (`>>`)
   ```python
   result = 5 >> 1  # result will be 2 (0101 >> 1 = 0010)
   ```

## Assignment Operations

Assignment operations are used to assign values to variables, often with a combination of arithmetic operations.

1. **Assign** (`=`)
   ```python
   x = 5  # Assigns 5 to x
   ```

2. **Add and Assign** (`+=`)
   ```python
   x += 3  # Equivalent to x = x + 3
   ```

3. **Subtract and Assign** (`-=`)
   ```python
   x -= 2  # Equivalent to x = x - 2
   ```

4. **Multiply and Assign** (`*=`)
   ```python
   x *= 4  # Equivalent to x = x * 4
   ```

5. **Divide and Assign** (`/=`)
   ```python
   x /= 5  # Equivalent to x = x / 5
   ```

6. **Modulus and Assign** (`%=`)
   ```python
   x %= 3  # Equivalent to x = x % 3
   ```

7. **Exponent and Assign** (`**=`)
   ```python
   x **= 2  # Equivalent to x = x ** 2
   ```

## Conclusion

Python supports a wide range of operations that you can perform on your data, from basic arithmetic to more complex bitwise manipulations. Understanding these operations is essential for writing efficient and effective Python code.




# Python Lists, Sets, Dictionaries, and Tuples

Python provides several built-in data structures that allow you to store and manipulate collections of data. Here are four commonly used ones: lists, sets, dictionaries, and tuples.

## 1. Lists

A list is an ordered, mutable collection of items. Lists can contain elements of different types.

### Creating a List

```python
# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# Creating a list of mixed data types
mixed_list = [1, "Hello", 3.14, True]
```

### Accessing List Elements

You can access elements in a list using their index (starting from 0).

```python
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry
```

### Modifying a List

Lists are mutable, so you can change their contents.

```python
fruits[1] = "blueberry"  # Changing banana to blueberry
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
```

### Adding Elements to a List

```python
# Using append() to add an element to the end of the list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Using insert() to add an element at a specific index
fruits.insert(1, "grape")
print(fruits)  # Output: ['apple', 'grape', 'blueberry', 'cherry', 'orange']
```

### Removing Elements from a List

```python
# Using remove() to remove a specific element
fruits.remove("blueberry")
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'orange']

# Using pop() to remove an element by index
fruits.pop(2)
print(fruits)  # Output: ['apple', 'grape', 'orange']
```

### List Comprehensions

List comprehensions provide a concise way to create lists.

```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

## 2. Sets

A set is an unordered collection of unique items.

### Creating a Set

```python
# Creating a set of integers
numbers = {1, 2, 3, 4, 5}

# Creating a set from a list (duplicates are removed)
unique_numbers = set([1, 2, 2, 3, 4, 4, 5])
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
```

### Adding Elements to a Set

```python
numbers.add(6)
print(numbers)  # Output: {1, 2, 3, 4, 5, 6}
```

### Removing Elements from a Set

```python
numbers.remove(4)
print(numbers)  # Output: {1, 2, 3, 5, 6}

# Using discard() (no error if the element doesn't exist)
numbers.discard(10)
print(numbers)  # Output: {1, 2, 3, 5, 6}
```

### Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

# Union
print(a | b)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(a & b)  # Output: {3}

# Difference
print(a - b)  # Output: {1, 2}

# Symmetric Difference
print(a ^ b)  # Output: {1, 2, 4, 5}
```

## 3. Dictionaries

A dictionary is an unordered collection of key-value pairs.

### Creating a Dictionary

```python
# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "profession": "Engineer"
}
```

### Accessing Dictionary Elements

```python
print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 25
```

### Modifying a Dictionary

```python
# Changing the value associated with a key
person["age"] = 26

# Adding a new key-value pair
person["city"] = "New York"

print(person)  # Output: {'name': 'Alice', 'age': 26, 'profession': 'Engineer', 'city': 'New York'}
```

### Removing Elements from a Dictionary

```python
# Using pop() to remove a key-value pair
person.pop("profession")
print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}
```

### Iterating Over a Dictionary

```python
# Iterating over keys
for key in person:
    print(key)

# Iterating over values
for value in person.values():
    print(value)

# Iterating over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

## 4. Tuples

A tuple is an ordered, immutable collection of items.

### Creating a Tuple

```python
# Creating a tuple
coordinates = (10.0, 20.0)

# Creating a tuple with mixed data types
person = ("Alice", 25, "Engineer")
```

### Accessing Tuple Elements

```python
print(coordinates[0])  # Output: 10.0
print(person[2])  # Output: Engineer
```

### Modifying a Tuple

Tuples are immutable, so you can't change their contents directly. However, you can create a new tuple by concatenating existing ones.

```python
new_person = person + ("New York",)
print(new_person)  # Output: ('Alice', 25, 'Engineer', 'New York')
```

### Unpacking Tuples

```python
name, age, profession = person
print(name)  # Output: Alice
print(age)  # Output: 25
print(profession)  # Output: Engineer
```

## Conclusion

Understanding and effectively using lists, sets, dictionaries, and tuples in Python can greatly enhance your ability to manipulate and organize data. Each of these data structures has its unique characteristics and use cases, making Python a powerful and flexible language for various programming tasks.




# Loops in Python

Python provides two types of loops for iterating over a block of code: the `for` loop and the `while` loop.

## 1. For Loop

A `for` loop is used for iterating over a sequence (such as a list, tuple, string, or range). It executes the block of code multiple times for each item in the sequence.

### Basic Syntax

```python
for item in sequence:
    # Code to be executed
```

### Example: Iterating Over a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

### Example: Using Range

The `range` function generates a sequence of numbers.

```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

### Example: Nested For Loop

You can nest `for` loops to iterate over multiple sequences.

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

**Output:**
```
i: 0, j: 0
i: 0, j: 1
i: 1, j: 0
i: 1, j: 1
i: 2, j: 0
i: 2, j: 1
```

## 2. While Loop

A `while` loop executes a block of code as long as a specified condition is true.

### Basic Syntax

```python
while condition:
    # Code to be executed
```

### Example: Basic While Loop

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

**Output:**
```
0
1
2
3
4
```

### Example: Infinite Loop with Break

To prevent an infinite loop, use the `break` statement to exit the loop when a condition is met.

```python
count = 0

while True:
    print(count)
    count += 1
    if count >= 5:
        break
```

**Output:**
```
0
1
2
3
4
```

### Example: While Loop with Else

The `else` block is executed when the loop condition becomes false.

```python
count = 0

while count < 5:
    print(count)
    count += 1
else:
    print("Loop is finished")
```

**Output:**
```
0
1
2
3
4
Loop is finished
```

## Conclusion

Understanding `for` loops and `while` loops is crucial for efficiently iterating over data in Python. The `for` loop is ideal for iterating over a fixed sequence of elements, while the `while` loop is useful for executing a block of code as long as a condition is met. Both types of loops can be combined with `break`, `continue`, and `else` statements to create complex control flows.




# Conditional Statements in Python

## 1. If Conditions

The `if` statement is used for decision-making operations. It allows you to execute a block of code only if a certain condition is met.

### Basic Syntax

```python
if condition:
    # Code to be executed if condition is true
```

### Example: If Statement

```python
age = 18

if age >= 18:
    print("You are an adult.")
```

**Output:**
```
You are an adult.
```

### Example: If-Else Statement

```python
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

**Output:**
```
You are a minor.
```

### Example: If-Elif-Else Statement

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

**Output:**
```
Grade: B
```

### Nested If Statements

You can nest `if` statements within each other.

```python
num = 10

if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Non-positive number")
```

**Output:**
```
Positive number
Even number
```

## 2. Match Statements

The `match` statement, introduced in Python 3.10, provides a more readable and concise way to handle multiple conditions. It is similar to switch-case statements found in other programming languages.

### Basic Syntax

```python
match variable:
    case value1:
        # Code to be executed if variable == value1
    case value2:
        # Code to be executed if variable == value2
    case _:
        # Code to be executed if none of the above cases match (default case)
```

### Example: Basic Match Statement

```python
day = "Monday"

match day:
    case "Monday":
        print("Start of the workweek.")
    case "Friday":
        print("End of the workweek.")
    case _:
        print("Midweek day.")
```

**Output:**
```
Start of the workweek.
```

### Example: Match Statement with Multiple Patterns

```python
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown status code")
```

**Output:**
```
Not Found
```

### Example: Match Statement with Pattern Matching

```python
point = (2, 3)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"X-axis at {x}")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")
    case _:
        print("Unknown point")
```

**Output:**
```
Point at (2, 3)
```

## Conclusion

Understanding `if` conditions and `match` statements in Python is essential for effective decision-making in your programs. The `if` statement allows you to execute code based on specific conditions, while the `match` statement provides a more elegant way to handle multiple possible values of a variable.
