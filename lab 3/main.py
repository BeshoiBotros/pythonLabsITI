from task1 import math_automation
from task2 import regex_log_cleaner
from task3 import datetime_reminder
from task4 import product_data_transformer
from task5 import os_file_manager
from task6 import random_data_generator


if __name__ == "__main__":
	tasks = {
		1: ("Math Automation", math_automation),
		2: ("Regex Log Cleaner", regex_log_cleaner),
		3: ("Datetime Reminder", datetime_reminder),
		4: ("Product Data Transformer", product_data_transformer),
		5: ("OS File Manager", os_file_manager),
		6: ("Random Data Generator", random_data_generator)
	}

	print("Available Tasks:")
	for num, (name, _) in tasks.items():
		print(f"{num}) {name}")

	while True:
		try:
			choice = int(input("Select task number: "))
			if choice not in tasks:
				raise ValueError
			break
		except ValueError:
			print("Invalid choice. Try again.")

	print(f"Running {tasks[choice][0]}...")
	tasks[choice][1]()