# Ask user to input 3 numbers. Detremine what is the highest number

# Pseudocode

# Ask user for input

number1 = input("What's the first number?: ")
number2 = input("What's the second number?: ")
number3 = input("What's the third number?: ")

# Determine the highest number
# if number1 is the highest
if number1 >= number2 and number1 >= number3:
    print(f"The biggest number is: {number1}")

# if number2 is the highest
if number2 >= number1 and number2 >= number3:
    print(f"The biggest number is: {number2}")
# if number3 is the highest
if number3 >= number2 and number3 >= number1:
    print(f"The biggest number is: {number3}")

# else if all equal