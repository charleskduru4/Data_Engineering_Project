# Variable and Data type

# first_name : str = "John Charles"
# height : int = None

# print(first_name, height)

"""
A python variable is created automatically 
when you assign a value to it. The equal(=) is used to assign 
values to variable or a variable is a reserved memory area 
(memory address to store value)
""" 

"""
Creating python Variable: We can assign a value to the variable
we can use the assignment operator = to assign a value to a variable 
""" 
# counter : int = 100
# miles : float = 1000.0
# name: str = "Peter"

# # To print the variables value
# # print(counter, miles, name)

# print(miles)
# print(name)
# print(counter)

"""
Changing the value of a variable: Python variable are dynamically
typed and not subject to the data type restriction.
"""
var : int = 10
print(var)
# print its type
print(type(var))

# Assign different integer value to var
var: int = 55
print(var)

# Change var to string
var: str = "This is example of a string"
print(var)

# print its type
print(type(var))

#Change var to float
var:float = 35.69
print(var)

# print its type
print(type(var))

"""
Create Number, String, list variable
Number is a data type that store numeric value which can be of the type:
int --> integer
float --> decimal
complex
"""
# Example of integer:
age: int = 28
print(age)
print(type(age))

# Float are value with decimal
# create float variable
salary: float = 10800.77
print(salary)
print(type(salary))

"""
String variable in python is a set of characters represented in quotation mark.
python allows us to define a string in either pair of single or double.
To retrieve a piece of string from a given string, we can use the slice [] or [:]
To concatenate two string, we can use the addition(+) operator. 
"""
# Create a variable of the type string
str = 'PYnative'
# print the full string
print(str)
# Print the first character of the string
print(str[0])

# print character starting from 2nd to 5th
print(str[2:5])

# To print the length of the string
print(len(str))

# To concatenate string
print(str + "TEST")

"""
List type variable to represent a group of element or value as a single entity we should 
go for list variable type. For example, we can use to store student names.
The character of list:
1. Insertion order of element is preserved
2. Heterogenous is allow (int, float, string)
3. duplication of elements are permitted
4. List is mutable(can change)
5. List element should be enclose within a square bracket
"""
# Example
the_list = ['Jesse', 20, 40, 'Charles', 'Jessica', 50, 10.5]

# To print the complete list
print(the_list)

# To access 1st element of a list
print(the_list[0])

# to access the last element on the list
print(the_list[-1])

# To access chunks of element in the list
print(the_list[1:4])

# To modify first element in the list
the_list[0] = 'Micheal'
print(the_list[0])

# To add one or more element into the list
the_list.append(100)
print(the_list)

    
    
    