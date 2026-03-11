import json
import os

LIB_FILE = "library.json"
AVAILABLE_FILE = "available_books.txt"

print("СИСТЕМА УЧЁТА КНИГ В БИБЛИОТЕКЕ")
print("=" * 50)


def load_library():
    if not os.path.exists(LIB_FILE):
        return []

    try:
        with open(LIB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            print("Ошибка: неверный формат файла library.json (ожидается список).")
            return []
    except json.JSONDecodeError:
        print("Ошибка: не удалось прочитать JSON (файл повреждён или пуст).")
        return []


def save_library(books):
    with open(LIB_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


def get_next_id(books):
    if not books:
        return 1
    return max(book.get("id", 0) for book in books) + 1


def show_all_books(books):
    if not books:
        print("\nБиблиотека пуста.")
        return

    print("\nВСЕ КНИГИ:")
    print("-" * 50)
    for book in books:
        status = "доступна" if book.get("available", True) else "взята"
        print(f"ID: {book.get('id')}")
        print(f"Название: {book.get('title')}")
        print(f"Автор: {book.get('author')}")
        print(f"Год: {book.get('year')}")
        print(f"Статус: {status}")
        print("-" * 50)


def search_books(books):

    query = input("\nВведите автора или название для поиска: ").strip().lower()
    if not query:
        print("Поисковый запрос не может быть пустым.")
        return

    found = []
    for book in books:
        title = str(book.get("title", "")).lower()
        author = str(book.get("author", "")).lower()
        if query in title or query in author:
            found.append(book)

    if not found:
        print("Книги по запросу не найдены.")
        return

    print("\nНАЙДЕННЫЕ КНИГИ:")
    print("-" * 50)
    for book in found:
        status = "доступна" if book.get("available", True) else "взята"
        print(f"ID: {book.get('id')}")
        print(f"Название: {book.get('title')}")
        print(f"Автор: {book.get('author')}")
        print(f"Год: {book.get('year')}")
        print(f"Статус: {status}")
        print("-" * 50)


def add_book(books):
    """Добавление новой книги."""
    print("\nДОБАВЛЕНИЕ НОВОЙ КНИГИ")
    title = input("Введите название книги: ").strip()
    author = input("Введите автора: ").strip()
    year_str = input("Введите год издания: ").strip()

    if not title or not author or not year_str:
        print("Ошибка: название, автор и год не могут быть пустыми.")
        return

    try:
        year = int(year_str)
    except ValueError:
        print("Ошибка: год должен быть целым числом.")
        return

    new_book = {
        "id": get_next_id(books),
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }

    books.append(new_book)
    save_library(books)
    print("Книга успешно добавлена и сохранена в библиотеке.")


def change_availability(books):
    if not books:
        print("\nБиблиотека пуста. Нечего менять.")
        return

    try:
        book_id = int(input("\nВведите ID книги для изменения статуса: "))
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return

    for book in books:
        if book.get("id") == book_id:
            current = book.get("available", True)
            book["available"] = not current
            save_library(books)
            new_status = "доступна" if book["available"] else "взята"
            print(f"Статус книги изменён. Теперь книга {new_status}.")
            return

    print("Книга с таким ID не найдена.")


def delete_book(books):
    if not books:
        print("\nБиблиотека пуста. Нечего удалять.")
        return

    try:
        book_id = int(input("\nВведите ID книги для удаления: "))
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return

    for i, book in enumerate(books):
        if book.get("id") == book_id:
            print(f"Книга '{book.get('title')}' будет удалена.")
            books.pop(i)
            save_library(books)
            print("Книга удалена из библиотеки.")
            return

    print("Книга с таким ID не найдена.")


def export_available_books(books):

    available_books = [b for b in books if b.get("available", True)]

    if not available_books:
        print("\nНет доступных книг для экспорта.")
        return

    with open(AVAILABLE_FILE, "w", encoding="utf-8") as f:
        for b in available_books:
            f.write(f"{b.get('id')} - {b.get('title')} "
                    f"({b.get('author')}, {b.get('year')})\n")

    print(f"\nСписок доступных книг сохранён в файл '{AVAILABLE_FILE}'.")


books = load_library()

while True:
    print("\n" + "-" * 50)
    print("МЕНЮ:")
    print("1. Просмотр всех книг")
    print("2. Поиск по автору/названию")
    print("3. Добавить новую книгу")
    print("4. Изменить статус доступности (взята/возвращена)")
    print("5. Удалить книгу по ID")
    print("6. Экспорт доступных книг в файл")
    print("7. Выйти")

    choice = input("\nВыберите действие (1-7): ").strip()

    if choice == "1":
        show_all_books(books)
    elif choice == "2":
        search_books(books)
    elif choice == "3":
        add_book(books)
    elif choice == "4":
        change_availability(books)
    elif choice == "5":
        delete_book(books)
    elif choice == "6":
        export_available_books(books)
    elif choice == "7":
        print("Программа завершена!")
        break
    else:
        print("Ошибка: выберите номер от 1 до 7.")
