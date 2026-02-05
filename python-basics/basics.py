print("Let's start our jurny")
print("---------------------")

# Variable, assignment Comments:
# ------------------------------

x = 4
y = 3
z=[1,2,3]
w =[ "a","b","c"]
i=0
# a = "Look"
# a = str(x)
# print(type(a))
# a= int(23)
# a= float(23)
# a= complex(23)
# a = None
# a = True
# a = 10
# print(isinstance(a,int))



# Global function:
# -----------------
# a = input("What do you want: ")
# print(dir(x))
# help(str)
# print(len(x))
# print(id(x))
# print(id(y))
# help(object)
# code = """
# for i in range(3):
#     print("Hello", i)
# """
# exec(code)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p = Person("Alice", 25)
# print(vars(p))
# def test():
#     a = 1
#     b = 2
#     print(locals())
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p = Person("Alice", 25)
# print(vars(p))
# test()
# print(globals())
# print(a)


"""
Operators
---------
"""
# print(x+y)
# x*=x
# if (x != i):
#     print("True")
# text = "machine learning"
# print("machine" in text)
# print(2 in z)
# print(12 not in z)
# print(x is  y)
# print(x is not y)
# print(x<<3)
# print(x<<2)
# print(5 ^ 3)
# nums = [1, 2, 3, 2, 1]
# unique = 0
# for n in nums:
#     unique ^= n
# print(unique)

"""
String methods
--------------
"""
# a = input("Input your idea: ")
# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a.capitalize())
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())
# print(a.split())
# print("Python".isalpha())
# text = "hello world"
# print(text.startswith("hello"))
# name = input("Enter your name: ")
# print(text.find("a")) 
# c = "xyxPythonxy"
# print(c.strip("xy")) 
# num = "42"
# print(num.zfill(5))
# filename = "report.pdf"
# if filename.startswith("report"):
# print("This is a report file")
# text = "hello-world-python"
# result = text.partition("-")
# print(result)
# print(text.ljust(10, "-"))


"""
control flow
------------
"""

# if(x>10):
#     print(f"{x} is the learger")
# elif(x<=4):
#     print(f"{x} is smaller")

# for i in range(5):
#     print(i)
# else:
#     print("this is the end")
# for i in z:
#     if i==3:
#         print("found")
#         break
# else:
#     print("not found")
# while x == 4:
#     for i in range (10):
#         print(i)
#     x+=1
# try:
#     x = int(input("Enter a positive number: "))
#     if x < 0:
#         raise ValueError("x cannot be negative")
#     print(10 / x)
# except ValueError as ve:
#     print("Value Error:", ve)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# finally:
#     print("Execution finished")

"""
Functions
---------
"""
# def greet(name):
#     print(f"{name} Hello")
# greet("Arnobdas_dev")
# def add(a,b):
#     x = a+b
#     return x
# print(add(1,2))
# sqr = lambda x: x**2
# print(sqr(5))
# def add(*args):
#     return sum(args)
# print(add(1, 2, 3, 4))
# def person_info( **kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# person_info(name="arnob", age=25)
# def change_global():
#     global x
#     x += 5
# change_global()
# print(x)
# def count_up_to(n):
#     for i in range(1, n+1):
#         x=+ i 
# for num in count_up_to(5):
#     print(num)
# class Person:
#     name = "Alice"
# p = Person()
# print(getattr(p, "name"))     
# print(getattr(p, "age", 25))
# setattr(p, "age", 30)
# print(p.age)
# print(hasattr(p, "name"))   
# print(hasattr(p, "gender")) 
# delattr(p, "age")
# print(hasattr(p, "age"))
# class user:
#     pass
# u = user()
# setattr(u,"username", "admin")
# setattr(u, "email", "admin@gmail.com")
# if hasattr(u,"email"):
#     print(getattr(u,"email"))
# delattr(u,"email")
# print(hasattr(u,"email"))
# print(getattr(u,"username"))
# for key, value in u.__dict__.items():
#     if value == "admin":
#         print(key)

"""
List methods
------------
"""
# list = ["apple", "mango", "orange"]
# number = [ 1,2,3,3,1,2,5,3,4,9]
# list.append("litchi")
# list.extend(["banana","litchi"])
# list.insert(1,"tomato")
# list.remove("apple")
# list.pop(1)
# list.index("litchi")
# number = number + [2,3,4,4,4,4]
# print(number.count(3))
# print(list)
# number.sort()
# number.reverse()
# # b =number.copy()
# b = [x for x in number if number.count(x)==1]
# print(b)

"""
Tuple methods
-------------
"""
# tuple = ("mango","tometo")
# a,b = tuple
# # print(a)
# # print(b)
# print(tuple.count("mango"))
# print(tuple.index("mango"))

"""
Set methods
-----------
"""
# fruits = { "mango", "lemon"}
# num = {1,2,3,4}
# fruits.add("orange")
# fruits.update({"litchi"},["goava"])
# fruits.remove("mango")
# fruits.discard("tomato")
# fruit = fruits.pop()
# print(fruits)
# print(fruit)
# print(fruits.union(num))
# print(fruits.intersection(num))
# print(fruits.difference(num))
# print(fruits.symmetric_difference(num))
# print(fruits.isdisjoint(num))
# print(fruits.issubset(num))
# print(fruits.issuperset(num))
# fruits.clear()


"""
Dictionary methods
------------------
"""
# my_dic ={
#     "name": "Arnob",
#     "age": 25
# }
# new_dic = my_dic.copy()
# print(new_dic)
# print(my_dic.get("name"))
# print(my_dic.items())
# print(my_dic.keys())
# print(my_dic.values())
# name = my_dic.pop("name")
# age = my_dic.popitem()
# my_dic.setdefault("age", 30)
# print(name)
# print(age)
# my_dic.update([("age",25),("age",2444)])
# print(my_dic)

"""
File I/O
--------
"""
# with open("home.txt", "a") as file:
#     file.write("this is dfdsfsdfsdarnob.\n")
# with open("home.txt", "a") as file:
#     file.write("New line added\n")
# with open("home.txt", "r") as file:
#     data = file.read(1)          
    # print(data)
    # print(file.readline(4))
    # print(file.readline(4))
    # print(file.readlines(4))
    # file.seek(0)
    # print(file.read())
    # print(file.tell())
# with open("home.txt","w"):
#     file.write("hiii")
#     file.flush()
# import os
# if os.path.exists("home.txt"):
#     print("File available")
#     os.remove("home.txt")
# with open("new.txt", "w") as file:
#     os.write(file, b"Hhiiiiii")

"""
Date and time
-------------
"""
import datetime
import time
# time = datetime.datetime.now()
# time = datetime.date.today()
# time = datetime.datetime(2025,12,2,4,5,5)
# time = datetime.timedelta()
# print(time)
# print(time.ctime())
# print(time.sleep(2))
# # print(time.year)
# print(time.month)
# print(time.day)
# print(time.hour)
# print(time.minute)
# print(time.second)
# print(time.microsecond)
import calendar
# print(calendar.month(2025,1))
# print(calendar.isleap(2024))
# from datetime import datetime
# while True:
#     now = datetime.now().strftime("%H:%M")
#     if now == "02:13":
#         print("Wake up!")
#         break
#     time.sleep(30)

"""
Exceptions
----------
"""
# try:
#     x = 12/0
# except ZeroDivisionError:
#     print("You can not devided by zero")
# raise ValueError("0 can not useable")
# raise TypeError("This is type error")
# raise IndexError("Index out of range")
# raise KeyError("Key not found")
# raise NameError("Variable not defined")
# raise AttributeError("Object has no attribute")
# raise FileNotFoundError("File not found")
# raise IOError("I/O error")
# raise OSError("OS error")
# raise ImportError("Module not found")
# raise KeyboardInterrupt("User stopped program")
# raise MemoryError("Out of memory")

"""
CSV
---
"""
import csv
# with open("students.csv","r") as file:
#     # reader = csv.reader(file)
#     reader = csv.DictReader(file)
#     # next(reader)
#     for row in reader:
#         print(row)
# with open("student's.csv","w+", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "age", "selary"])                EEEEEEEEEEEE
#     writer.writerow(["Asrnob",25,3450])
#     new = csv.DictReader(writer)
#     for tk in writer:
#         print(tk)

# data = [
#     {"name": "Arnob", "age": 20, "score": 85},
#     {"name": "Rafi", "age": 21, "score": 90}
# ]
# with open("students.csv", "w", newline="") as file:  EEEEEEEEEEEEEEEEEEE
#     name = ["name", "age", "score"]
#     writer = csv.DictWriter(file, fieldnames=name)
#     writer.writeheader()
#     writer.writerow(data)
import json
data = {
    "name": "Arnob",
    "age": 20,
    "skills": ["Python", "ML"]
}
# with open("data.json", "w") as file:
#     json.dump(data, file)
# with open("data.json","r") as file:
#     data = json.load(file)
# print(data)
# print(data["name"])
# with open("data.json", "w") as file:
#     json.dump(data,file, indent =2)
# json_str = json.dumps(data)
# print(type(json_str))
# obj = json.loads(json_str)
# print(type(obj))

# print( " Now everything is perfect ... ")
# class dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
# d = dog("Tom", 3)
# print(d.__dict__)

# class Employee:
#     company = "Basundhara"
#     @classmethod
#     def changeCompany(cls, newCompany):
#         cls.company = newCompany
# Employee.changeCompany("Jamuna")
# print(Employee.company)
# Employee.__name__ = "worker"
# print(Employee.__name__)