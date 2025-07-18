# Q1 Write a function that returns True if a number is even and a multiple of 5.
def number_is_even_and_multiple_of_5(a):
a = input("Enter a number: ")
a = int(a)
if a % 2 == 0 and a % 5 == 0:
    print(True)
else:
    print(False)

#Q2 Write a program that asks the user for a number and checks:
#If it is positive, negative, or zero.

a = input("Enter a number: ")
a = int(a)
if a > 0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")    
  

#Q3 Write a program that asks the user to enter a year and checks if it is a leap year or not.
Year = int(input("Enter a year: "))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print("Leap Year")

#Q4 
