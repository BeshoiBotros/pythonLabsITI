import math
from task7 import log_time


@log_time
def math_automation():
	while True:
		numbers_input = input("Enter numbers (comma separated): ")
		try:
			numbers = [float(num.strip()) for num in numbers_input.split(",")]
			break
		except ValueError:
			print("Invalid input. Please enter valid numbers.")

	with open("math_report.txt", "w") as f:
		for num in numbers:
			f.write(f"Number: {num}\n")
			f.write(f" Floor: {math.floor(num)}\n")
			f.write(f" Ceil: {math.ceil(num)}\n")
			f.write(f" Square root: {math.sqrt(num):.2f}\n")
			f.write(f" Area of circle: {math.pi * num * num:.2f}\n\n")

	print("math_report.txt created successfully. Contents:")
	with open("math_report.txt", "r") as f:
		print(f.read())