import csv
import random


def random_data_generator():
	while True:
		try:
			count = int(input("How many random numbers to generate? "))
			if count <= 0:
				raise ValueError
			break
		except ValueError:
			print("Enter a valid positive integer.")

	numbers = [random.randint(1, 100) for _ in range(count)]

	with open("random_numbers.csv", "w", newline="") as f:
		writer = csv.writer(f)
		writer.writerow(["index", "value"])
		for i, num in enumerate(numbers, start=1):
			writer.writerow([i, num])

	print(f"Generated {count} numbers. Average = {sum(numbers)/count:.2f}")