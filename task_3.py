print("ПРОГРАММА УПРАВЛЕНИЯ ТОВАРАМИ")
print("=" * 50)

try:
    with open('products.csv', 'r', encoding='utf-8') as f:
        pass
    print("Файл products.csv уже существует")
except FileNotFoundError:
    print("Создаю файл products.csv с примерными данными")
    with open('products.csv', 'w', encoding='utf-8') as f:
        f.write("Название Цена Количество\n")
        f.write("Яблоки 100 50\n")
        f.write("Бананы 80 30\n")
        f.write("Молоко 120 20\n")
        f.write("Хлеб 40 100\n")
    print("Файл создан!")
except Exception as e:
    print(f"Ошибка: {e}")
    exit()

print("-" * 50)


def read_products():
    products = []
    with open('products.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line:
            data = line.split()
            if len(data) == 3:
                name = data[0]
                price = int(data[1])
                quantity = int(data[2])
                products.append([name, price, quantity])
    return products


def save_products(products):
    with open('products.csv', 'w', encoding='utf-8') as f:
        f.write("Название Цена Количество\n")
        for p in products:
            f.write(f"{p[0]} {p[1]} {p[2]}\n")


while True:
    print("\nМЕНЮ:")
    print("1. Показать все товары")
    print("2. Добавить новый товар")
    print("3. Найти товар по названию")
    print("4. Общая стоимость товаров на складе")
    print("5. Выйти")

    choice = input("\nВыберите действие (1-5): ")

    if choice == "1":
        products = read_products()
        print("\nСПИСОК ТОВАРОВ:")
        print("Название\tЦена\tКоличество")
        print("-" * 40)
        for p in products:
            print(f"{p[0]}\t\t{p[1]}\t{p[2]}")

    elif choice == "2":
        products = read_products()

        name = input("Введите название товара: ")
        if not name:
            print("Ошибка: название не может быть пустым")
            continue

        try:
            price = int(input("Введите цену: "))
            quantity = int(input("Введите количество: "))
            if price < 0 or quantity < 0:
                print("Ошибка: цена и количество должны быть положительными")
                continue
        except ValueError:
            print("Ошибка: введите числа")
            continue

        products.append([name, price, quantity])
        save_products(products)
        print(f"Товар '{name}' добавлен!")

    elif choice == "3":
        products = read_products()

        search = input("Введите название товара для поиска: ").lower()
        if not search:
            print("Ошибка: введите название")
            continue

        found = False
        print("\nРЕЗУЛЬТАТЫ ПОИСКА:")
        for p in products:
            if search in p[0].lower():
                print(f"{p[0]} - Цена: {p[1]}, Количество: {p[2]}")
                found = True

        if not found:
            print("Товары не найдены")

    elif choice == "4":
        products = read_products()

        total = 0
        for p in products:
            total += p[1] * p[2]

        print(f"\nОБЩАЯ СТОИМОСТЬ ТОВАРОВ НА СКЛАДЕ: {total} руб.")

        print("\nДетали:")
        for p in products:
            cost = p[1] * p[2]
            print(f"{p[0]}: {p[1]} руб × {p[2]} шт = {cost} руб")

    elif choice == "5":
        print("Программа завершена!")
        break

    else:
        print("Ошибка: выберите 1-5")

print("=" * 50)
