#### start python problem sovling
# =======================================================
# =======================================================
# =======================================================
# =======================================================
###   Get quotient of division of two numbers

# def get_quotient(num1, num2):

#     if num1 == 0 or num2 == 0:
#         return "Zero is not divided by any number"
#     else:
#         return int(num1 / num2)

# print(get_quotient(10, 3)) # 3
# print(get_quotient(10, 5)) # 2
# print(get_quotient(0, 5)) # 2

# =======================================================
# =======================================================
# =======================================================
# =======================================================

# Input four numbers and generate the sum of these

# def inpt_four_numbers(num1, num2, num3, num4):
#     x = num1 + num2 + num3 + num4
#     print(x)
    
# inpt_four_numbers(2, 19, 4, 77)



# =======================================================
# =======================================================
# =======================================================
# =======================================================

#   Sum and average of marks of five students taken from the user

# a = int(input("Enter 1st student marks: "))
# b = int(input("Enter 2nd student marks: "))
# c = int(input("Enter 3rd student marks: "))
# d = int(input("Enter 4th student marks: "))

# sm = a + b + c + d
# print("Total of student marks:", sm)

# averag = sm / 4
# print("Average of student: ", averag)

# percentage = float(sm / 1100 * 100)
# print(percentage)
# =======================================================
# =======================================================
# =======================================================
# =======================================================

# Check if a number is greater than 80, say “good”, if not say, “Try again”

# def greater_number(num):
#     if num > 80:
#         print("good")
#     else:
#         print("Try Again")

# greater_number(50)
# greater_number(91)



# =======================================================
# =======================================================
# =======================================================
# =======================================================

# Check whether a number is divisible by another user-given number or not
# def divisible_num(num1, num2):
#     if num1 % num2 == 0:
#         print("Divisible number")
#     else:
#         print("Not divisible number")

# divisible_num(10, 2)




# =======================================================
# =======================================================
# =======================================================
# =======================================================

# Sum of odd numbers from 10 user-given numbers

#  Sum of odd numbers from 10 user-given numbers

# def odd_numbers(numbers):
#     total = 0
#     for x in range(numbers):
#         if x % 2 != 0:
#             print("Odd number:", x)
#             total += x
#     print("Total of odd numbers:", total)

# odd_numbers(10)




# =======================================================
# =======================================================
# =======================================================
# =======================================================


# Sum of even number from n user-given numbers. Where n is also user-input.
# users = int(input("Enter a number:"))
# print(users)

# total = 0
# for x in range(users):
# 	if x % 2 == 0:
#          print("Even number:", x)
#          total += x
# print("Total of even numbers:", total)
    
# =======================================================
# =======================================================
# =======================================================

#  Show first n terms of Fibonacci series

# def fibonancci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=" ")
#         a,b = b, a + b
# fibonancci(10) 




# ===============================================
# =======================================================
# =======================================================

# Converting temperature from Fahrenheit to Celsius [Formula: C = (f-32) * (5/9)]

# def fahrenheit_to_celciusa(f):
#     C = (f - 32) * (5/9)
#     return C
# print(fahrenheit_to_celciusa(33))





# =======================================================
# =======================================================
# =======================================================

#  Calculating pay for an employee, given the hours worked and rate per hour.

#  Calculating pay for an employee, given the hours worked and rate per hour.

# def calculate_pay(hours, rate):
#     if hours > 40:
#         overtime_hours = hours - 40
#         regular_hours = 40
#         overtime_pay = overtime_hours * (rate * 1.5)
#         regular_pay = regular_hours * rate
#         total_pay = regular_pay + overtime_pay
#         return total_pay
#     else: 
#         regular_pay = hours * rate
#         return regular_pay
# print(calculate_pay(45, 10))
# print(calculate_pay(33, 5))



# =======================================================
# =======================================================
# =======================================================


# Determine the status of a student (pass or fail) given his/her marks in a subject (passing marks = 50)

# def student_status(marks):
#     if marks > 50:
#         print("pass")
#     else: 
#         print("fail")
# student_status(60)
# student_status(44)


# =======================================================
# =======================================================
# =======================================================





# =======================================================
# =======================================================
# =======================================================
# =======================================================
# =======================================================
# =======================================================
# =======================================================
# =======================================================
# =======================================================