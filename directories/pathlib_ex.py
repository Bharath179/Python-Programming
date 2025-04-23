from pathlib import Path

# Create a new directory named 'example_dir' using pathlib
# Path("directory").mkdir(exist_ok=True)  # `exist_ok=True` prevents error if directory exists
# print("Directory 'directory' created")

# Check if 'example_dir' exists using pathlib
# path = Path("directory")
# if path.exists() and path.is_dir():
#     print("It's a directory.")
# else:
#     print("Directory does not exist.")

# List contents of the current directory using pathlib
path = Path(".")
for entry in path.iterdir():
    print(entry.name)