class MyClass:
    def __init__(self):
        self.public_variable = "I am public"
        self._protected_variable = "I am protected"
        self.__private_variable = "I am private"

    def get_private_variable(self):
        return self.__private_variable


# Outside the class
obj = MyClass()

# Public variable (accessible)
print(obj.public_variable)

# Protected variable (conventionally not accessed directly)
print(obj._protected_variable)

# Attempting to access private variable directly will raise an AttributeError
# print(obj.__private_variable)  # This line would result in an error

# Accessing private variable using a method
print(obj.get_private_variable())
