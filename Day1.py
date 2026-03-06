# This is to reverse a string
text = input("Enter a word: ")
print(text[::-1])

# This is to check if a string is palindrome
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# This is to check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# This is to count characters
text = input("Enter the text:")
print("Length of the text: ", len(text))

# This is to swap 2 numbers
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
A, B = B, A
print("First number: ", A, "Second number", B)

# Build calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter operator (+ , -, /, *): ")
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
