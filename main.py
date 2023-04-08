import sys
import os

if len(sys.argv) == 2:
    # Get the filename from the command-line argument
    filename = sys.argv[1]

    # Check if the file exists
    if not os.path.isfile(filename):
        print(f"Error: {filename} does not exist")
        sys.exit(1)

    # Check if the user has read permissions for the file
    if not os.access(filename, os.R_OK):
        print(f"Error: {filename} access denied")
        sys.exit(1)
else:
    print("Usage: python script.py <filename>")
    sys.exit(1)

# If we got here, the file exists and is readable
print(f"{filename} exists and is readable")

# python main.py filenamecheck.txt

