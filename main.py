def split_combo_file(combo_file='combo.txt'):
    with open(combo_file, 'r') as file:
        lines = file.readlines()
    with open('userpass.txt', 'w') as userpass_file, \
         open('cookie.txt', 'w') as cookie_file, \
         open('user.txt', 'w') as user_file:
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) >= 3:
                userpass_file.write(f"{parts[0]}:{parts[1]}\n")
                cookie_file.write(f"{parts[2]}:{''.join(parts[3:])}\n")
                user_file.write(f"{parts[0]}\n")
split_combo_file()
