<h1 align="center">
<table>
<tr>
<td>
This script is a basic example of the Python programming language It was created for personal use But feel free to use or study it
</td>
</tr>
</table>

---

<h1 align="center">
  <br>
  Features
  <br>
</h1>

> [!NOTE]  
> **This program is not designed for everyone It might seem a bit confusing I will update the program to make it more user-friendly and visually appealing next time**

* Deleting Files: It defines a function to delete files if they exist, and it prints a message indicating whether each file was deleted or did not exist.
* Creating Files: It has another function to create a new file if it does not already exist. It prompts the user to enter data line by line until the user types 'done'. The data is then written to the file.
* Splitting a Combo File: There is a function that reads a file named 'Combo.txt' and splits its content into three separate files:
  - 'UserPass.txt' for storing usernames and passwords.
  - 'Cookie.txt' for storing cookies.
  - 'Username.txt' for storing just usernames.
* Main Function: The main function orchestrates the execution. It deletes any existing relevant files, creates a new 'Combo.txt' file, processes it by splitting its content into separate files, and then prints a success message. The program waits for the user to press Enter before exiting.

---

<h1 align="center">
  <br>
  How To Use
  <br>
</h1>

![screenshot](https://github.com/vouvy/Split-Account/blob/main/Img/Split-Account.gif?raw=true)

> [!TIP]
> **If message is "Files have been processed successfully," this indicates that the process is complete You can now see the results**

---

<h1 align="center">
  <br>
  Code Example
  <br>
</h1>

```python
import os  # Import the os module to interact with the operating system.

def delete_files(file_paths):
    # Define a function to delete files given a list of file paths.
    for file_path in file_paths:
        # Loop through each file path in the provided list.
        if os.path.exists(file_path):
            # Check if the file exists.
            os.remove(file_path)
            # If the file exists, delete it.
            print(f"{file_path} has been deleted.")
            # Print a message confirming the file has been deleted.
        else:
            print(f"{file_path} does not exist.")
            # If the file does not exist, print a message indicating this.

def create_file(file_path):
    # Define a function to create a new file at the given path.
    print(f"{file_path} does not exist. Creating {file_path}.")
    # Inform the user that the file does not exist and will be created.
    with open(file_path, 'w', encoding='utf-8') as f:
        # Open the file for writing with UTF-8 encoding.
        while True:
            line = input(f"Enter data for {file_path} (type 'done' to finish): ")
            # Prompt the user to enter data for the file.
            if line.lower() == 'done':
                break
                # If the user types 'done', exit the loop.
            f.write(line + '\n')
            # Write the input line to the file, followed by a newline character.

def split_combo_file(combo_file='Combo.txt'):
    # Define a function to split the contents of the combo file into separate files.
    with open(combo_file, 'r', encoding='utf-8') as file:
        # Open the combo file for reading with UTF-8 encoding.
        lines = file.readlines()
        # Read all lines from the combo file into a list.
    with open('UserPass.txt', 'w', encoding='utf-8') as userpass_file, \
         open('Cookie.txt', 'w', encoding='utf-8') as cookie_file, \
         open('Username.txt', 'w', encoding='utf-8') as user_file:
        # Open three new files for writing with UTF-8 encoding.
        for line in lines:
            # Loop through each line in the combo file.
            parts = line.strip().split(':')
            # Split the line by colons and remove leading/trailing whitespace.
            if len(parts) >= 3:
                userpass_file.write(f"{parts[0]}:{parts[1]}\n")
                # Write the first two parts to the UserPass.txt file, separated by a colon.
                cookie_file.write(f"{parts[2]}:{''.join(parts[3:])}\n")
                # Write the third part and any remaining parts (joined together) to the Cookie.txt file.
                user_file.write(f"{parts[0]}\n")
                # Write the first part (username) to the Username.txt file.

def main():
    # Define the main function.
    combo_file = 'Combo.txt'
    # Specify the name of the combo file.
    files_to_delete = [combo_file, 'UserPass.txt', 'Cookie.txt', 'Username.txt']
    # List of files to be deleted.
    delete_files(files_to_delete)
    # Call the delete_files function to delete the listed files.
    create_file(combo_file)
    # Call the create_file function to create the combo file.
    split_combo_file(combo_file)
    # Call the split_combo_file function to process and split the combo file.
    print("Files have been processed successfully.")
    # Print a success message.
    input("Press Enter to exit...")
    # Wait for the user to press Enter before closing the program.

if __name__ == "__main__":
    main()
    # Check if this script is being run directly (not imported as a module) and if so, call the main function.
```
