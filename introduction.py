# print("-------------------------------print function----------------------------------")
# print("GeeeksforGeeks \n is best for DSA content.")
# print ("GeeeksforGeeks is best for DSA content")
# print ("GeeeksforGeeks is best for DSA content", end="**")
# print("Welcome to GFG")

# print("-------------------------------input----------------------------------")

# val = input("Enter your value: ")
# print(val)

# #program to check input type in python
# num = input ("Enter number :")

# print(num)
# print("Type of val variable")
# print(type(val))
# print("Type of num variable")
# print(type(num))

# # type casting 

# #take input from user
# input_a = input("Enter an integer for type cast")


# #print data type
# print(type(input_a))

# #type cast into integer
# input_a = int(input_a)

# #print data type
# print(type(input_a))

# ######## implicit type conversion #########
# x = 10
# print("x is of type:",type(x))

# y = 10.6
# print("y is of type:",type(y))

# z = x + y
# print(z)
# print("z is of type:",type(z))


# ########expllicit type conversion #########
# s = "10010"
# c = int(s,2)
# print ("After converting to integer base 2 : ", end="")
# print (c)

# e = float(s)
# print ("After converting to float : ", end="")
# print (e)

# #python code to demonstrate type conversion using tuple(), set(), list()
# #initializing string
# s = "geeks"

# #Printing sting converting to tuple
# c = tuple(s)
# print("After converting string to tuple :",end="")
# print (c)

# #printing string converting to sets
# c = set(s)
# print ("After converting string to set :", end="")
# print (c)

# #printing string converting to list
# c = list(s)
# print ("After converting string to list :",end="")
# print (c)

# #Python docstring
# def multiply(a, b):
#     """Multiplies the value of a and b"""
#     return a*b
# #pting the docstring of multiply function
# print(multiply.__doc__)


#if statement
if 10 > 5:
    print("10 is greater than 5")
print("Program ended")


#if..else statement example
x = 3
if x == 4:
    print("Yes")
else:
    print("No")
print("Program ended")

#nested if statemenet
num = 10

if num > 5:
    print("Bigger than 5")

    if num <=15:
        print("Between 5 and 15")

#if-elif statement
 
letter = "A"

if letter == "B":
    print("Letter is B")
elif letter == "C":
    print("letter is C")
elif letter == "A":
    print("Letter is A")

else:
    print("Letter isn't A, B or C")

print('GeeksforGeeks')


String1 = "GeeksForGeeks"
print (String1[0])

def f():pass
print(type(f()))

print(1//2 + 1.0/2)