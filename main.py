import os
def delete_files(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} has been deleted.")
        else:
            print(f"{file_path} does not exist.")
def create_file(file_path):
    print(f"{file_path} does not exist. Creating {file_path}.")
    with open(file_path, 'w', encoding='utf-8') as f:
        while True:
            line = input(f"Enter data for {file_path} (type 'done' to finish): ")
            if line.lower() == 'done':
                break
            f.write(line + '\n')
def split_combo_file(combo_file='Combo.txt'):
    with open(combo_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('UserPass.txt', 'w', encoding='utf-8') as userpass_file, \
         open('Cookie.txt', 'w', encoding='utf-8') as cookie_file, \
         open('Username.txt', 'w', encoding='utf-8') as user_file:
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) >= 3:
                userpass_file.write(f"{parts[0]}:{parts[1]}\n")
                cookie_file.write(f"{parts[2]}:{''.join(parts[3:])}\n")
                user_file.write(f"{parts[0]}\n")
def main():
    combo_file = 'Combo.txt'
    files_to_delete = [combo_file, 'UserPass.txt', 'Cookie.txt', 'Username.txt']
    delete_files(files_to_delete)
    create_file(combo_file)
    split_combo_file(combo_file)
    print("Files have been processed successfully.")
    input("Press Enter to exit...")
if __name__ == "__main__":
    main()
