print("Let's start our jurny")
print("---------------------")

# Variable, assignment Comments:
# ------------------------------

x = 4
y = 3
z=[1,2,3]
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
-----------
"""
my_dic ={
    "name": "Arnob",
    "age": 25

}
new_dic = my_dic.copy()
print(new_dic)
print(my_dic.get("name"))
print(my_dic.items())
print(my_dic.keys())
print(my_dic.values())
name = my_dic.pop("name")
age = my_dic.popitem()
my_dic.setdefault("age", 30)
print(name)
print(age)
my_dic.update([("age",25),("age",2444)])
print(my_dic)