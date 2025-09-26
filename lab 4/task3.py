from datetime import datetime


def datetime_reminder():
	while True:
		date_input = input("Enter a date (YYYY-MM-DD): ")
		try:
			reminder_date = datetime.strptime(date_input, "%Y-%m-%d").date()
			break
		except ValueError:
			print("Invalid date format. Try again.")

	today = datetime.today().date()
	days_left = (reminder_date - today).days

	if days_left < 0:
		print("This date has already passed.")
	else:
		with open("reminders.txt", "a") as f:
			f.write(f"{reminder_date} -> {days_left} days left\n")
		print(f"Reminder saved: {reminder_date} -> {days_left} days left")
