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

# Finding the sum of 10 numbers taken from the user.

# put = int(input("Enter a number:"))
# print(put)

# summ = 0

# for i in range(put):
#     summ += i
#     print(summ)




# =======================================================
# =======================================================
# =======================================================


# Finding the sum of n numbers taken from the user. Where n is taken from the user as well.


# put = int(input("Enter a number:"))
# print(put)

# summ = 0

# for i in range(put):
#     summ += i
#     print(summ)
#     if summ == 10:
#         print("Total sum of numbers:", summ)

    

# =======================================================
# =======================================================
# =======================================================


#  Calculate the factorial of a positive integer entered by the user.

# summ = int(input("Enter the number: "))
           
# print(summ)

# a = summ * (summ - 1) * (summ -2) * (summ - 3) * (summ - 4)
# print(a)

# =======================================================
# =======================================================
# =======================================================
# =======================================================

# tasks = []

# def show_menu():
#     print("Start TODO List")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Exit")

# while True:
#     show_menu()
#     choice = input("Enter your choice: " )
#     if choice == '1':
#         task = input("Enter your task: ")
#         tasks.append(task)
#         print("Task added successfully!")
#     elif choice == '2':
#         print("\nView Tasks")
#         for i, task in enumerate(tasks, start=1):      # mean of enumerate ==  range(len(tasks))
#             print(f"{i}. {task}")
#     else:
#         if choice == 'exit':
#             break

# print(tasks)


# =======================================================
# =======================================================
# =======================================================

#  Project: Number Guessing Game


# import random

# number = random.randint(0, 100)

# print("Guess a number between", number)

# zero = 0
# print("Guess the number between 1 to 100")

# while True:
#     guess = int(input("Enter your guess: "))
#     zero += 1
#     if guess < number:
#         print("Low number!")
#     elif guess > number:
#         print("High number!")
#     else:
#         print("Corret to guess the number") 
#         break



# =======================================================
# =======================================================
# =======================================================

#  Project: Simple Calculator
# 📝 Description:
# Make a calculator that can do:

# Addition

# Subtraction

# Multiplication

# Division

# ✅ Features:
# User selects an operation

# Inputs two numbers

# Shows result

# Runs in a loop until user quits


# def add(x, y):
#     return x + y
# def sub(x, y):
#     return x - y
# def multi(x, y):
#     return x * y
# def divid(x, y):
#     if y == 0:
#         return ("Error! Division by zero is not allowed.")
#     return x / y
  

  
# number = int(input("enter first number: "))
# number2 = int(input("enter second number: "))

# while True:
#     print("\n📱 Simple Calculator")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")

#     array  = ['1','2','3','4','5']
#     choice = input("Enter choice(1/2/3/4/5): ")

#     if choice not in array:
#         print("Invalid Input")

#     if choice == '1':
#         print("Add" , add(number, number2))
#     elif choice == '2':
#         print("Subtract", sub(number, number2))
#     elif choice == '3':
#         print("Multiply", multi(number,number2))
#     elif choice == '4':
#         print("Divide" , divid(number,number2))
#     elif choice == '5':
#         print("Exit")
#         break
#     else:
#         print("Invalid choice! Please try again.")   







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
# =======================================================
# =======================================================
# =======================================================
# =======================================================
# =======================================================
# =======================================================
# =======================================================
# =======================================================