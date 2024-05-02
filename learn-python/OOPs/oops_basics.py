# class attributes, static methodds

# class Student:
#     college = "DMPS"
#     name = "anonymous" 

#     def __init__(self, age, name = None):
#         self.name = name if name is not None else Student.name
#         self.age = age

#     @staticmethod
#     def get_college():
#         return Student.college

# s1 = Student(age = 10)
# print(s1.name)
# print(s1.get_college())




# closure -  Inner function can access the variables and methods of its outer function and remembers its values.

# def outer(msg):
#     coumnt = 0

#     def inner():
#         nonlocal count  # Use nonlocal to indicate we're modifying the count variable in the outer scope
#         count += 1
#         return count

#     return increment

# # Usage
# counter1 = counter()
# print(counter1())  # Output: 1
# print(counter1())  # Output: 2

# counter2 = counter()
# print(counter2())






# __private/_protected

# class MyClass:
#     def __init__(self):
#         self.__private_var = 10

#     def __change_private_method(self):
#         self.__private_var = 20

#     def access_private_method(self):
#         self.__change_private_method()
#         print(self.__private_var)
    


# obj = MyClass()
# # Accessing private variable (name mangling applied)
# print(obj._MyClass__private_var)  # Output: 10
# # Accessing private method (name mangling applied)
# obj.access_private_method()  # Output: 20







#property decorator - to make attribute changes automatically detectable

class Circle:
    def __init__(self, pi):
        self.pi = pi

    @property
    def pi2(self):
        """Getter method for the radius."""
        return self.pi*self.pi

# Usage
circle = Circle(5)
print(circle.pi2)  # Output: 5

circle.pi = 10 
print(circle.pi2)  #






# duck-typing - means if object having certain methods enforced then it is duck-typed

# method overloading not supported in python

# dunder func. are inbuilt funcs to define the behavior of a class and a object, you can change that based on your needs (operator overloading)