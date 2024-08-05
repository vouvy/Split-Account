<table>
<tr>
<td>
This script is a basic example of the Python programming language. It was created for personal use, but feel free to use or study it
</td>
</tr>
</table>

---

## Features

- Read the Input File: It reads the contents of combo.txt, where each line is expected to contain data separated by colons (:).
- Split and Write Data: For each line:
 - It splits the line into parts based on colons.
 - If there are at least four parts:
 - It writes the first two parts (username and password) to userpass.txt.
 - It writes the third part (cookie) along with any additional parts to cookie.txt.
 - It writes the first part (username) to user.txt.
- File Outputs: The function creates three new files (userpass.txt, cookie.txt, and user.txt) and writes the processed information into these files.

## Code Example:

```python
def split_combo_file(combo_file='combo.txt'):  # Define a function named split_combo_file with an optional parameter combo_file that defaults to 'combo.txt'
    with open(combo_file, 'r') as file:  # Open the file specified by combo_file in read mode and assign it to the variable file
        lines = file.readlines()  # Read all lines from the file and store them in the list variable lines
    
    # Open three files in write mode: 'userpass.txt', 'cookie.txt', and 'user.txt'
    # Assign file handles to the variables userpass_file, cookie_file, and user_file respectively
    with open('userpass.txt', 'w') as userpass_file, \
         open('cookie.txt', 'w') as cookie_file, \
         open('user.txt', 'w') as user_file:
        
        for line in lines:  # Iterate over each line in the lines list
            parts = line.strip().split(':')  # Remove any leading/trailing whitespace from the line, then split it into parts using ':' as the delimiter
            
            if len(parts) >= 3:  # Check if the number of parts is at least 3
                # Write the first and second parts to 'userpass.txt', separated by ':'
                userpass_file.write(f"{parts[0]}:{parts[1]}\n")
                # Write the third part followed by the concatenation of all subsequent parts to 'cookie.txt', separated by ':'
                cookie_file.write(f"{parts[2]}:{''.join(parts[3:])}\n")
                # Write the first part to 'user.txt'
                user_file.write(f"{parts[0]}\n")

split_combo_file()  # Call the function to execute it with the default combo_file parameter
```
