import re
from task7 import log_time


@log_time
def regex_log_cleaner():
	
	fake_logs = [
		"user@example.com - success",
		"invalid-email - error",
		"admin@domain.org - login",
		"hello world",
		"test123@mail.com",
		"123@abc",
		"contact@company.com",
		"fake@@mail.com",
		"support@helpdesk.net",
		"notanemail"
	]

	with open("access.log", "w") as f:
		f.write("\n".join(fake_logs))

	# Extract valid emails
	with open("access.log", "r") as f:
		data = f.read()
		emails = re.findall(r"[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}", data)

	unique_emails = set(emails)

	with open("valid_emails.txt", "w") as f:
		f.write("\n".join(unique_emails))

	print(f"Found {len(unique_emails)} unique valid emails.")