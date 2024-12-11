import re
import requests

def check_string(password):
    pattern = pattern = r"^(?=\S{8,15}$)(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_\-+=])[A-Za-z\d!@#$%^&*()_\-+=]+$"
    a = re.findall(pattern, password)
    print("Found matches:",a)
    return a

def check_file(path):
    try:
        with open(path, encoding="utf-8") as file:
            s = file.read()
            return check_string(s)
    except Exception as e:
        return f"Ошибка открытия файла: {e}"


def check_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return check_string(response.text)
    except Exception as e:
        return f"Ошибка загрузки страницы: {e}"

def main():
    print("Выберите действие:")
    print("1. Проверить пароль")
    print("2. Проверить файл")
    print("3. Проверить URL")
    choice = input("Введите номер действия: ")
    if choice == "1":
        password = input("Введите пароль: ")
        print("Пароль надёжный" if check_string(password) else "Пароль ненадёжный")
    elif choice == "2":
        file_path = input("Введите путь к файлу: ")
        print("Найденные надёжные пароли:", check_file(file_path))
    elif choice == "3":
        url = input("Введите URL: ")
        print("Найденные надёжные пароли:", check_url(url))
    else:
        print("Неверный выбор. Завершение программы.")

if __name__ == "__main__":
    main()