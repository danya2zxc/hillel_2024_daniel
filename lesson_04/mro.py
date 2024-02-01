import time
from pathlib import Path

user_input = input("Enter the string for search: ")

file_path = Path("rockyou.txt")

start_time = time.time()

try:
    with file_path.open(
        mode="r", encoding="utf-8", errors="ignore"
    ) as new_file:
        found_lines = 0
        for index, line in enumerate(new_file, 1):
            if user_input in line:
                found_lines += 1
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
else:
    end_time = time.time()
    print(
        f"While going through the entire file '{'rockyou.txt'}', "
        f"lines were found {found_lines} mentioning your request "
        f"'{user_input}'"
    )
    print(f"time spent on the operation: {end_time - start_time} seconds")
