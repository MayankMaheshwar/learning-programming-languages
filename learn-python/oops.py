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

def outer(msg):
    coumnt = 0

    def inner():
        nonlocal count  # Use nonlocal to indicate we're modifying the count variable in the outer scope
        count += 1
        return count

    return increment

# Usage
counter1 = counter()
print(counter1())  # Output: 1
print(counter1())  # Output: 2

counter2 = counter()
print(counter2())