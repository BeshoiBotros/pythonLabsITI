import math


# 1
print("Hello World")

# 2
binary_input = input("Enter a number in binary form: ")
try:
	decimal_number = int(binary_input, 2)
	print(f"Decimal: {decimal_number}")
except ValueError:
	print("Invalid binary number.")

# 3
def fizzbuzz(num):
	if num % 3 == 0 and num % 5 == 0:
		return "FizzBuzz"
	elif num % 3 == 0:
		return "Fizz"
	elif num % 5 == 0:
		return "buzz"
	else:
		return str(num)

number = int(input("Enter a number for FizzBuzz: "))
print(fizzbuzz(number))

# 4
radius_input = input("Enter the radius of a circle: ")
try:
	radius = float(radius_input)
	area = math.pi * radius ** 2
	c = 2 * math.pi * radius
	print(f"Area: {area}")
	print(f"Circumference: {c}")
except ValueError:
	print("Invalid radius.")

# 5
def is_valid_name(name):
	return name.isalpha() and name.strip() != ""
def is_valid_email(email: str):
	if not email.endswith('@gmail.com'):
		return False
	return True

while True:
	user_name = input("Enter your name: ")
	user_email = input("Enter your email: ")
	if is_valid_name(user_name) and is_valid_email(user_email):
		print("Name confirmed. and email")
		break
	else:
		print("Invalid name or email.")
    


print(f"Name: {user_name}\nEmail: {user_email}")

# 6
main_string = input("Enter a string: ")
count_iti = main_string.count('iti')
print(f"'iti' occurs {count_iti} times.")
