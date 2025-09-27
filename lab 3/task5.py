import os
import shutil

    
def os_file_manager():
	while True:
		path = input("Enter directory path: ").strip()
		if os.path.isdir(path):
			break
		else:
			print("Invalid directory. Try again.")

	backup_dir = os.path.join(path, "backup")
	os.makedirs(backup_dir, exist_ok=True)

	copied = 0
	for file in os.listdir(path):
		if file.endswith(".txt"):
			shutil.copy(os.path.join(path, file), backup_dir)
			copied += 1

	print(f"Copied {copied} .txt files to backup directory.")