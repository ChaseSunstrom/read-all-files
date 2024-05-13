import os

# Prompt the user for the directory to search
search_directory = input("Enter the directory to search (default: current directory): ")
if not search_directory:
    search_directory = os.getcwd()

# Prompt the user for the directory to export the output file
export_directory = input("Enter the directory to export the output file (default: C:/output): ")
if not export_directory:
    export_directory = "C:/output"  # Use a subdirectory within C:/

# Create the export directory if it doesn't exist
os.makedirs(export_directory, exist_ok=True)

# Specify the output file name
output_file = os.path.join(export_directory, "output.txt")

total_words = 0

# Recursively search subdirectories and process files
for root, dirs, files in os.walk(search_directory):
    for filename in files:
        file_path = os.path.join(root, filename)

        # Read the contents of the file
        with open(file_path, 'r') as file:
            contents = file.read()

        # Count the number of words in the file
        word_count = len(contents.split())
        total_words += word_count

        # Get the file extension
        _, extension = os.path.splitext(filename)

        # Append the file name, extension, and contents to the output file
        with open(output_file, 'a') as output:
            output.write(f"File: {filename}\n")
            output.write(f"Extension: {extension}\n")
            output.write(f"Contents:\n{contents}\n")
            output.write(f"File Name: {filename}\n")
            output.write("\n")

print(f"File contents appended to {output_file}")
print(f"Total words appended: {total_words}")