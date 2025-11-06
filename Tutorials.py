#TASK 1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add = a+b
sub = a-b
mul = a*b
div = a/b

print("Addition: ", add)
print("Multiplication: ", mul)
print("Subtraction: ", sub)
print("Division: ", div)

#TASK2
a= input("Enter first name: ")
b= input("Enter last name: ")
c = a + " " + b
print("Hello, ",c,"! You are lucky.")

#TASK3 1.
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n = int(input("Enter a number: "))
x = factorial(n)
print(f"Factorial of {n} is: {x}")

#2. 
import math
num = int(input("Enter a number: "))

sqrt_num= math.sqrt(num)
sine_num = math.sin(num)
log_num = math.log(num)

print(f"Square root of {num} is: {sqrt_num}")
print(f"Sin of {num} is: {sine_num}")
print(f"Log  of {num} is: {log_num}")