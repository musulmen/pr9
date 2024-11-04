import re

while True:
    email = input("Введите email (или введите 'exit' для выхода): ")
    
    if email.lower() == 'exit':
        break

    pattern = r"^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$"
    match = re.match(pattern, email)

    if match:
        username = match.group(1)
        domain = match.group(2)
        print(f"username: {username}")
        print(f"domain: {domain}")
    else:
        print("Неверный формат email.")
