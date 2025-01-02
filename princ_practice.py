# number=int(input("enter the number:"))
# if number % 5 == 0:
#     if number % 2 == 0:
#         print(f"{number} is divisible by both two and five")
#     else:
#         print("this number is not divisible by 2!!")
# else:
#     print("this number is not divisible by five")
'''create a list if five fruit names and print it
'''
# fruit=['banana','mango','avocado','apple','orange']
# print(fruit)

'''
access and element the last element in the list ['apple,'banana','cherrry']
'''
# fruit=['banana','mango','avocado','apple','orange']
# print(fruit[-1])
'''
add
'''
# fruit=['banana','mango','avocado','apple','orange']
# fruit.append('kiwi')
# print(fruit)
'''
remove one item from a list
'''
# fruit=['banana','mango','avocado','apple','orange']
# fruit.remove('banana')
# print(fruit)
'''
use loop to print each item in the list
'''
# fruit=['banana','mango','avocado','apple','orange']
# for x in fruit :
#     print(x)
'''
create a list of numbers from 1 to 10 and print only the even numbers
'''
# num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in num :
#     if x%2==0:
#         print(x)
#     else:
#         continue
'''
reverse the list
'''
# fruit=['banana','mango','avocado','apple','orange']
# fruit.reverse()
# print(fruit)
'''
combine the two lists
'''
# list1=[1, 2, 3]
# list2=[4, 5, 6]
# add=list1+list2
# print(add)
'''
("extend" key word used to add two lists)

-->>modify the list
'''
# List=[5, 10, 15]
# List[1]=12
# print(List)

'''
find the lingth of list and print it
'''
# alphabet=['a', 'b', 'c', 'd', 'e']
# print(len(alphabet))

'''
use list comprehension to generate a list of square for numbers for numbers from 1 to 10, excluding numbers divisible by 3
'''
# numbers=[x**2 for x in range(11) if x%3!=0]
# print(numbers)

'''

'''
# li=[[1, 2],[3, 4],[5,6]]
# new=li[0]+li[1]+li[2]
# print(new)
'''
///////////////////////set/////////////////set////////////////////set///////////////////////
'''
'''create a list and print it'''
# vegetable={'cabbage', 'carrot', 'garlic,' 'onion', 'tomato'}
# print(vegetable)
'''add an item to the list'''
# fruit={'apple', 'banana', 'cherry'}
# fruit.add('mango')
# print(fruit)
'''list items in a set'''
# prog={'python', 'java', 'c++'}
# for x in prog:
#     print(x)
'''remove an item from a set using remove/discard'''
# fruit={'apple', 'banana', 'cherry'}
# fruit.remove('cherry')
# print(fruit)
'''check the index of an item'''
# fruit={'apple', 'banana', 'cherry'}
# print('banana' in fruit)
'''combine the set using union'''
# num={1, 2, 4}
# num1={3, 5, 6}
# print(num.union(num1))
'''find an intersection'''
# num={1, 2, 3, 4}
# num1={4, 5, 6, 7}
# print(num.intersection(num1))
'''use the difference() method'''
# num={1, 2, 3, 4}
# num1={3, 4, 5, 6}
# print(num.difference(num1))
'''using clear'''
# sets={1, 2, 3, 4, 5, 6}
# print(sets.clear())
'''filter the repeated number'''
# lists=[1, 2, 3, 6, 3, 4, 6]
# uni= []
# for x in lists :
#     if x not in uni:
#         uni.append(x)
#     else:
#         print(x)
'''access the single vaalue of the tuple'''
# tup=(1, 2, 3, 4, 5)
# print(tup[1])
'''slice the tuple'''
# tup=(1, 2, 3, 4, 5)
# tup1=tup[1:3]
# print(tup1)
'''index'''
# tup=(1, 2, 3, 4, 5)
# print(1 in tup)
'''intersection'''
# num={1, 2, 3, 4}
# num1={3, 4, 5, 6}
# print(num.intersection(num1))
''''''
# num={1, 2, 3, 4}
# num1={3, 4, 5, 6}
# print(num&num1)
'''///Hard Exercice///'''
'''filter repeated letter using set'''
# li=input('enter your word:  ')
# se=set(li)
# print(se)
'''symmetric difference'''
# a={'abebe','fitsum','tesema','arega'}
# b={'fitsum','ayele','tesema','kebede'}
# print(a.symmetric_difference(b))
'''////////////Tuple///////////////Tuple//////////////Tuple/////////'''
'''length n tuple'''
# tup=('dog','cow','cat')
# print(len(tup))
'''Write a function to check if two tuples have at least one common item.'''
# tup=('dog','cow','cat')
# tup1=('cow','hen','sheep')
# for x in tup:
#     if x in tup1:
#         print(x)
'''Convert a tuple of strings to uppercase: `("hello", "world") → ("HELLO", "WORLD")`.'''
# tup=('hello')
# tup1=('world')
# Tup=tup.upper()
# Tup1=tup1.upper()
# print(Tup , end=' ')
# print(Tup1)
'''Write a program to find the unique elements in two tuples.'''
# tup=('dog','cow','cat')
# tup1=('cow','hen','sheep')
# Tup= tup + tup1
# Tup=set(Tup)
# tup=tuple(Tup)
# print(Tup)
''' Implement a function that takes a tuple and returns a new tuple with only even numbers.'''
# tup=(1, 2, 3, 4, 5, 6, 7, 8)
# for x in tup:
#     if x % 2 ==0:
#         print(x)
'''Create a tuple of mixed data types and filter out only the string elements.'''
# tup=(1, 'cow', 0.3, 'red', 2)
# for x in tup:
#     if type(x)== int or type(x) == float:
#         print(x)
'''//////Dictionary/////////Dictionary/////////Dictionary//////'''
'''create an empty dictionary called dog'''
# dog={}
# print(type(dog))
'''add name,color,breed, legs,age'''
# dog={}
# dog['name']=' '
# dog['color']=' '
# dog['legs']=' '
# dog['age']=' '
# print(dog)