# source link where i have learn these all the topics:
# https://drive.google.com/drive/folders/1LahwPSc6f9nkxBiRrz6LFUzkrg-Kzvov


# print("Hello, World!")
# print("*" * 10)
# print("*" * 10)
# x = 1
course = "Python for Beginners"
# print(x)
# print(course)
# print(len(course))
# print(course[0])
# print(course[-1])
# print(course[0:6])
# print(course[0:])
# print(course[:6])
# print(course[:])
# name = "Jennifer"
# print(name[1:-1])
# first = "John"
# last = "Smith"
# message = first + " [" + last + "] is a coder"
# print(message)
# msg = f"{first} [{last}] is a coder"
# print(msg)
# print(course.upper())
# print(course.lower())
# print(course.find("P"))
# print(course.find("p"))
# print(course.find("Python"))
# print(course.replace("for", "4"))
# print(course.replace("o", "0"))
# print("Python" in course)
# print(course.title())
# print(course.strip())
# print(course.lstrip())
# print(course.rstrip())
# print("hh" not in course)
# print(round(2.9))
# print(abs(-2.9))
# print(pow(3, 2))
# print(max(3, 2, 5, 1))
# print(min(3, 2, 5, 1))
# print(sum([3, 2, 5, 1]))
# x = input("Enter a value: ")
# print(type(x))
# print(f"You entered: {x}")
# Quiz: What are the primitives types in Python?
# int, float, bool, str
# Quiz: What are the output of the following code?
# fruit = "Apple"
# print(fruit[1])
# print(fruit[1:-1])
# print(10 % 3)
# temperature = 35
# if temperature > 30:
#     print("It's a hot day")
# elif temperature > 20:
#     print("It's a nice day")
# elif temperature > 10:
#     print("It's a bit cold")
# else:    print("It's cold")
# temperature = 35
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# print("Enjoy your day")
# age = 17
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("You are not old enough to vote")
#     print("Please come back in {} years".format(18 - age))
# age = 17
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not Eligible"

# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)

# age = 22 #ternary operator
# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)

# heigh_income = False
# good_credit = True
# student = True

# if student:
#     print("Student")
# if heigh_income and good_credit:
#     print("Eligible for loan")
# elif heigh_income or good_credit:
#     print("Maybe Eligible for loan")
# else:
#     print("Not Eligible for loan")

# if (heigh_income or good_credit) or not student:
#     message = "Eligible for loan"
# else:
#     message = "Not Eligible for loan"
# print(message)

# age = 17 # comparison operator
# if age >= 18 and age < 65:
#     print("Eligible")

# if 18 <= age < 65:
#     print("Eligible")
# print("Not Eligible")

# if False:
#     print("Hello")
# else:
#     print("Bye")

# success = False
# for i in range(3):
#     print("Attempt", i + 1, (i + 1) * ".")
#     if success:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")

# Nested loops
# for x in range(3):
#     for y in range(3):
#         print(f"({x}, {y})")

# iterate
# for x in range(5):
# for x in "Python":
# for x in [1, 2, 3, 4, 5]:
#     print(x)

# while loop
# i = 100
# while i > 0:
#     print(i)
#     i //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"We have {count} even numbers between 1 and 10")

# function
# def greet_user(name, last_name):
#     print(f"Hi {name} {last_name}!")
#     print("Welcome aboard")
# greet_user("John", "Smith")


# def sum_numbers(number1, number2):
#     return number1 + number2
# print(sum_numbers(3, 5))

# movies = []

# movie1 = input("Movie 1: ")
# movie2 = input("Movie 2: ")
# movie3 = input("Movie 3: ")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

# print(movies)

# movies = []
# movies.append(input("Movie 1: "))
# movies.append(input("Movie 2: "))
# movies.append(input("Movie 3: "))
# print(movies)
# movies.sort()
# print("Sorted: ", movies)
# movies.reverse()
# print("Reversed: ",movies)
# movies.insert(0, 0)
# print("Inserted 0 at the start: ", movies)
# movies.clear()
# print("Cleared movies: ", movies)

# tupple = (1, 2, 3)
# print(tupple)
# print(type(tupple))

# tuppleSingleValue = (1,)
# print(tuppleSingleValue)
# print(type(tuppleSingleValue))

# numbers = [1, 2, 2, 3, 4, 4] # remove duplicates from list
# unique_numbers = list(set(numbers))
# print(unique_numbers)

# dictionary
# info_obj = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True,
#     "list": [1, 2, 3],
#     "tuple": (1, 2, 3),
#     "object": {"key": "value"},
#     "float": 3.14,
#     10: "Ten",
#     10.5: "Ten Point Five",
#     True: "True Value",
#     (1, 2, 3): "Tuple Key",
#     "name": 'Jane Doe'  # This will overwrite the previous "name" key
# }
# print(info_obj)
# print(info_obj["object"])
# print(info_obj["object"]["key"])
# print(info_obj["name"] == info_obj.get("name"))
# print(info_obj.get("name") == 'John Smith')
# name = info_obj["name"] = "Leo Smith"
# print(info_obj)
# print(info_obj.keys()) # print all the keys in the dictionary
# print(info_obj.values()) # print all the values in the dictionary
# print(info_obj.items()) # print all the key-value pairs in the dictionary
# print(info_obj.get("name", "Not Found")) # get the value of the key "name" or return "Not Found" if the key is not found
# print(info_obj.update({"name": "ALI", "age": 25})) # update the value of the key "name" and "age"
# print(info_obj)
# print(len(info_obj["object"])) # print the number of key-value pairs in the dictionary
# print(len(list(info_obj.keys()))) # print the number of keys in the dictionary
# null_object = {}
# null_object["name"] = "Kartik"
# print(null_object)

# newList = [1, 2, 3, 4, 5]
# replaceValue = newList.copy()
# replaceValue[2] = 10
# print(replaceValue, newList)

# set Methods
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# print(collection)

# collection.remove(2)
# print(collection)

# collection.discard(3) # does not raise an error if the element is not found
# print(collection)

# collection.clear()
# print(collection)

# collection.pop() # removes and returns an arbitrary element from the set
# print(collection)

# what the difference between hashable and unhashable types in Python?
# Hashable types are immutable and can be used as keys in a dictionary or elements in a set. Unhashable types are mutable and cannot be used as keys in a dictionary or elements in a set. Examples of hashable types include int, float, str, tuple, and frozenset. Examples of unhashable types include list, dict, and set.
# mutable & immutable types in Python?
# Mutable types are those that can be changed after they are created. Examples of mutable types include list, dict, and set. Immutable types are those that cannot be changed after they are created.
# Examples of immutable types include int, float, str, tuple, and frozenset.

# collection = [1, 2, 3, 4, 5]
# collection.pop() # removes and returns an arbitrary element from the set
# print(collection)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print("Union:", set1.union(set2)) # returns a new set that contains all the elements from both sets
# print("Intersection:", set1.intersection(set2)) # returns a new set that contains only the elements that are present in both sets
# print("Difference:", set1.difference(set2)) # returns a new set that contains only the elements that are present in the first set but not in the second set
# print("Symmetric Difference:", set1.symmetric_difference(set2)) # returns a new set that contains only the elements that are present in either set but not in both sets

# Loop
# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print("Count:", n * i)
#     i += 1

# traverse a list using while loop
# nums = [1, 2, 3, 4, 5]

# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

# tuple of nums
# nums = (1, 2, 3, 4, 5)
# x = 3
# i = 0
# while i < len(nums):
#     if x == nums[i]:
#         print(f"Found {x} at index {i}")
#     i += 1

# break & continue
# nums = (1, 2, 3, 4, 5)
# x = 3
# i = 0
# while i < len(nums):
#     if x == nums[i]:
#         print(f"Found {x} at index {i}")
#         break
#     i += 1
# print("Loop ended")

# i = 1
# while i <= 10:
#     if i % 2 != 0:
#         i += 1
#         continue
#     print("Even num: ", i)
#     i += 1

# for i in range(1, 11):
#     if i % 2 != 0:
#         continue
#     print("Even num: ", i)

# list = [1, 2, 3, 4, 5]
# for num in list:
#     if num == 3:
#         break
#     print(num)
# print("Loop ended")

# str = "Pythonhhh"
# for char in str:
#     if char == "h":
#         continue
#     print(char)
# else:
#     print("Loop ended")

# nums = [1, 4, 16, 25, 36, 49, 64, 81, 100]
# for num in nums:
#     print(num)

# nums = (1, 4, 16, 25, 36, 49, 64, 81, 100)

# i = 0
# x = 36
# for val in nums:
#     if (val == x):
#         print("Found ", val, " at index ", i)
#         break
#     i += 1
# else:
#     print("36 not found")

# seq = range(10) # stop
# print(list(seq))
# for i in seq:
#     print(i)

# seq = range(1, 11) # start, stop
# print(list(seq))
# for i in seq:
#     print(i)

# seq = range(1, 11, 2) # start, stop, step
# print(list(seq))
# for i in seq:
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# make a calculator using for loop code must be small and advance logic concept implement
# for i in range(1, 4):
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     operator = input("Enter operator (+, -, *, /): ")

#     if operator == "+":
#         result = num1 + num2
#     elif operator == "-":
#         result = num1 - num2
#     elif operator == "*":
#         result = num1 * num2
#     elif operator == "/":
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             print("Error: Division by zero")
#             continue
#     else:
#         print("Invalid operator")
#         continue

#     print(f"Result: {result}")

# what outcome of next
# val = int(input("Enter a number less than 100: "))
# for i in range(val, 100+1):
#     print(i)

# file I/O
# f = open("file.txt", "r") # all types of file modes: r, w, a, x, b, t, + (read, write, append, exclusive creation, binary mode, text mode, read and write)
# f.write("Hello, World!\n")
# print(f.read(3)) # print(f.read()) # read the entire file
# print(f.readline()) # print(f.readlines()) # read all lines and return a list of lines
# f.write("Welcome to Python programming.\n")
# f.close()

# f = open("file.txt", "r")
# word = "Python"

# def check_word():
#    with open("file.txt", "r") as f:
#         content = f.read()
#         if word in content:
#             print(f"'{word}' is present in the file.")
#         else:
#             print(f"'{word}' is not present in the file.")
# check_word()

# def line_by_line():
#     with open("file.txt", "r") as f:
#         data = True
#         line_no = 1
#         while data:
#             data = f.readline()
#             if word in data:
#                 print(f"'{word}' is present in line {line_no}.")
#             line_no += 1
# line_by_line()

# count = 0
# with open("file.txt", "r") as f:
#     data = f.read()
#     nums = data.split(",")
#     if
#     for val in nums:
#         if (int(val) % 2 == 0):
#             count += 1
# print(f"Total even numbers: {count}")

# Class & Object
# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def greet(self):
#         print(
#             f"Hi, I'm {self.name} and I'm {self.age} years old, and my marks are {self.marks}.")


# student1 = Student("John", 20, 85)
# student1.greet()
# student2 = Student("Roman", 28, 90)
# student2.greet()


# Class with private attributes and methods, encapsulation, and inheritance, polymorphism, and abstraction.
# class Person:
#     def __init__(self, name, age):
#         self.__name = name  # private attribute
#         self.__age = age    # private attribute

#     def __greet(self):  # private method
#         print(f"Hi, I'm {self.__name} and I'm {self.__age} years old.")

#     def introduce(self):
#         self.__greet()  # calling the private method

# class Student(Person):  # inheritance
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)  # calling the parent class constructor
#         self.marks = marks

#     def introduce(self):  # method overriding (polymorphism)
#         super().introduce()  # calling the parent class method
#         print(f"My marks are {self.marks}.")
# student1 = Student("John", 20, 85)
# student1.introduce()

# inheritance concept
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def start_engine(self):
#         print("Engine started.")

# class Car(Vehicle):
#     def __init__(self, make, model, num_doors):
#         super().__init__(make, model)
#         self.num_doors = num_doors

#     def start_engine(self):
#         print("Car engine started.")

# car1 = Car("Toyota", "Camry", 4)
# car1.start_engine()  # Output: Car engine started.
# print("Name:", car1.make)  # Output: Toyota
# print("Model:", car1.model)  # Output: Camry
# print("Number of doors:", car1.num_doors)  # Output: 4

# list = (1, 2, 3, 4, 5)
# list1 = (6, 7, 8, 9, 10)
# list2 = [11, 21, 31, 41, 51]
# list3 = [61, 71, 81, 91, 101]

# merged_list = list + list1
# merged_lists = list2 + list3
# print(merged_list)
# print(merged_lists)

# create complex number class with addition, subtraction, multiplication, and division operations.

# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def __add__(self, other):
#         return ComplexNumber(self.real + other.real, self.imag + other.imag)

#     def __sub__(self, other):
#         return ComplexNumber(self.real - other.real, self.imag - other.imag)

#     def __mul__(self, other):
#         real_part = self.real * other.real - self.imag * other.imag
#         imag_part = self.real * other.imag + self.imag * other.real
#         return ComplexNumber(real_part, imag_part)

#     def __truediv__(self, other):
#         denominator = other.real**2 + other.imag**2
#         real_part = (self.real * other.real + self.imag * other.imag) / denominator
#         imag_part = (self.imag * other.real - self.real * other.imag) / denominator
#         return ComplexNumber(real_part, imag_part)

#     def __str__(self):
#         return f"{self.real}g + {self.imag}i"
    
# c1 = ComplexNumber(2, 3)
# c2 = ComplexNumber(4, 5)
# print("c1:", c1)  # Output: c1: 2 + 3i
# print("c2:", c2)  # Output: c2: 4 + 5i
# print("c1 + c2:", c1 + c2)  # Output: c1 + c2: 6 + 8i
# print("c1 - c2:", c1 - c2)  # Output: c1 - c2: -2 - 2i
# print("c1 * c2:", c1 * c2)  # Output: c1 * c2: -7 + 22i
# print("c1 / c2:", c1 / c2)  # Output: c1 / c2

# dandar function 

# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, order2):
#         return self.price > order2.price

# odr1 = Order("rise", 20)
# odr2 = Order("tea", 17)
# print(odr1 > odr2)  # Output: True