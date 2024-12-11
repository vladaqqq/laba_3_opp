import re
import requests

def check_string(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?!.*\s).{8,15}$"
    passwords = password.split()

    valid_passwords = []

    for password in passwords:
        if re.match(pattern, password):
            valid_passwords.append(password)

    if not valid_passwords:
        return f"Пароли не найдены"
    return f"Все найденные пароли: {valid_passwords}"


def check_file(path):
    valid_passwords = []
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?!.*\s).{8,15}$"
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                password = line.strip()
                if re.match(pattern, password):
                    valid_passwords.append(password)
            if not valid_passwords:
                return f"Пароли не найдены"
            return f"Все найденные пароли: {valid_passwords}"
    except Exception as e:
        return f"Ошибка открытия файла: {e}"


def check_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return check_string(response.text)
    except Exception as e:
        return f"Ошибка загрузки страницы: {e}"

