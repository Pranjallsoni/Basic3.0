Task 3 – Python Programs

This folder contains two simple Python programs demonstrating the use of recursion and the math module for mathematical computations.

📘 Program 1: Factorial of a Number (Using Recursion)
Description
This program calculates the factorial of a number entered by the user using a recursive function.

Code
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))
x = factorial(n)
print(f"Factorial of {n} is: {x}")

How It Works:
The user inputs a number `n`.
The function `factorial(n)` calls itself recursively until it reaches the base condition (`n == 0` or `n == 1`).
The program then prints the factorial of the number.



📗 Program 2: Mathematical Calculations Using `math` Module
Description
This program uses Python’s built-in `math` module to calculate the square root, sine, and natural logarithm (log base *e*) of a number entered by the user.

Code:
import math

num = int(input("Enter a number: "))

sqrt_num = math.sqrt(num)
sine_num = math.sin(num)
log_num = math.log(num)

print(f"Square root of {num} is: {sqrt_num}")
print(f"Sin of {num} is: {sine_num}")
print(f"Log of {num} is: {log_num}")

How It Works:
The program imports the `math` library.
The user enters a number.
The program computes:

Square root** using `math.sqrt(num)`
Sine (in radians)** using `math.sin(num)`
Natural logarithm** using `math.log(num)`
Finally, it displays all calculated results.

 ⚠️ Notes:
The logarithm function (`math.log()`) only works for positive numbers.
For better precision in trigonometric functions, make sure your input is in radians

Author
Pranjal Soni

