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
def count_up_to(n):
    for i in range(1, n+1):
        x=+ i  # pause here and give i

for num in count_up_to(5):
    print(num)
class Person:
    name = "Alice"
p = Person()
print(getattr(p, "name"))     
print(getattr(p, "age", 25))
setattr(p, "age", 30)
print(p.age)
print(hasattr(p, "name"))   # True
print(hasattr(p, "gender")) 