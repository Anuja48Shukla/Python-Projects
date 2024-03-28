# def my_function(fname, lname):
#     print("hello, my name is :", fname, lname)
# my_function("Anuja", "Shukla")
#
# def fruits(*fruitsname):
#     print("Fruits are:", fruitsname[1:3])
# fruits("Orange","Apple","Pear")

# def colors(**color):
#     print("2nd color is :", color["color2"])
# colors(color1 = "red", color2 = "blue")
#
# def my_function(country = "India"):
#     print("I live in :", country)
# my_function()
# my_function("Norway")

# def mylistfunction(color):
#     for x in color:
#         print(x)
#
# color = ["blue", "red", "orange"]
# mylistfunction(color)
#
# def add(a,b,c):
#     return a+b+c
# sum = add(3,6,4)
# print(sum)
#
# #pass
# def passexample():
#     pass

# def factorial_func(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_func(n-1)
#
# result = factorial_func(6)
# print("Factorial is:", result)

#Lambda
# b = lambda a : a+20
# print(b(3))
#
# add = lambda a,b : a + b
# sum = add(4,6)
# print(sum)
#
# def myfunc(n):
#     return lambda a : a* n
# square = myfunc(2)
# print(square(20))

class Myclass:
    x = 7
obj1 = Myclass()
print(obj1.x+3)

class Student:
    def __init__(myself,name, age, marks):
        myself.name = name
        myself.age = age
        myself.marks = marks

obj2 = Student("Ram", 21, 84.36)
print("Name is :", obj2.name)
print("Age is :", obj2.age)
print("Marks is :", obj2.marks)





















