from datetime import datetime

def write_log(operation, result):
    with open("calculator.log", "a", encoding="utf-8") as f:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time_now}] {operation} = {result}\n")


def show_last_operations():
    try:
        with open("calculator.log", "r", encoding="utf-8") as f:
            lines = f.readlines()

        if lines:
            print("\nПОСЛЕДНИЕ 5 ОПЕРАЦИЙ:")
            print("-" * 40)
            for line in lines[-5:]:
                print(line.strip())
        else:
            print("\nЛог-файл пуст")
    except FileNotFoundError:
        print("\nЛог-файл еще не создан")


def clear_log():
    try:
        open("calculator.log", "w").close()
        print("\nЛог-файл очищен!")
    except Exception as e:
        print(f"\nОшибка при очистке: {e}")


show_last_operations()

while True:
    print("\n" + "-" * 50)
    print("МЕНЮ:")
    print("1. Выполнить вычисление")
    print("2. Показать последние операции")
    print("3. Очистить лог-файл")
    print("4. Выйти")

    choice = input("\nВыберите действие (1-4): ")

    if choice == "1":
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите числа!")
            continue

        op = input("Введите операцию (+, -, *, /): ")

        result = None
        operation_str = ""

        if op == "+":
            result = num1 + num2
            operation_str = f"{num1} + {num2}"
        elif op == "-":
            result = num1 - num2
            operation_str = f"{num1} - {num2}"
        elif op == "*":
            result = num1 * num2
            operation_str = f"{num1} * {num2}"
        elif op == "/":
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                continue
            result = num1 / num2
            operation_str = f"{num1} / {num2}"
        else:
            print("Ошибка: неверная операция!")
            continue

        print(f"Результат: {operation_str} = {result}")
        write_log(operation_str, result)
        print("Операция записана в лог")

    elif choice == "2":
        show_last_operations()

    elif choice == "3":
        clear_log()

    elif choice == "4":
        print("Программа завершена!")
        break

    else:
        print("Ошибка: выберите 1-4")