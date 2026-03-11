try:
    with open("students.txt", "r", encoding="utf-8") as f:
        pass
    print("Файл students.txt уже существует")
except FileNotFoundError:
    print("Создаю файл students.txt с примерными данными")
    try:
        with open("students.txt", "w", encoding="utf-8") as f:
            f.write("Юсупова Саша:5,4,3,5\n")
            f.write("Петров Петр:4,3,4,4\n")
            f.write("Сидорова Мария:5,5,5,5\n")
            f.write("Демьяненко Алина:4,4,4,5\n")
            f.write("Иванов Иван:3,4,3,4\n")
        print("Файл создан!")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")
        exit()
except Exception as e:
    print(f"Ошибка при создании файла: {e}")
    exit()

print("-" * 40)

students = []
averages = []

try:
    with open("students.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        print("Файл students.txt пустой!")
        exit()

    print("Данные студентов:")
    valid_students_found = False

    for line_num, line in enumerate(lines, 1):
        line = line.strip()

        if not line:
            continue

        try:
            if ":" not in line:
                print(f"Строка {line_num} не содержит ':' - пропускаем")
                continue

            name_part, grades_text = line.split(":", 1)
            name = name_part.strip()

            if not name:
                print(f"Строка {line_num}: пустое имя - пропускаем")
                continue

            grades_list = [g.strip() for g in grades_text.split(",") if g.strip()]
            grades = []
            valid = True

            for g in grades_list:
                try:
                    grade = int(g)
                    if 1 <= grade <= 5:
                        grades.append(grade)
                    else:
                        print(f"Строка {line_num}: оценка {grade} вне диапазона 1-5 - пропускаем")
                        valid = False
                        break
                except ValueError:
                    print(f"Строка {line_num}: '{g}' не является числом - пропускаем")
                    valid = False
                    break

            if not valid or len(grades) == 0:
                continue

            avg = sum(grades) / len(grades)
            avg = round(avg, 2)

            students.append(name)
            averages.append(avg)
            valid_students_found = True

            print(f"{len(students)}. {name} - оценки: {grades}, средний балл: {avg}")

        except Exception as e:
            print(f"Ошибка в строке {line_num}: {e}")
            continue

    if not valid_students_found:
        print("Нет корректных данных о студентах!")
        exit()

except FileNotFoundError:
    print("Ошибка: Файл students.txt не найден!")
    exit()
except Exception as e:
    print(f"Ошибка при чтении файла: {e}")
    exit()

print("-" * 40)

if len(students) == 0:
    print("Нет данных для обработки")
    exit()

print("Студенты с баллом выше 4.0:")

try:
    with open(RESULT_FILE, "w", encoding="utf-8") as result_file:
        result_file.write("Студенты со средним баллом выше 4.0:\n")
        result_file.write("-" * 30 + "\n")

        count = 0
        for i in range(len(students)):
            if averages[i] > 4.0:
                count += 1
                text = f"{students[i]} - {averages[i]}"
                print(f"{count}. {text}")
                result_file.write(text + "\n")

        if count == 0:
            print("Нет таких студентов")
            result_file.write("Таких студентов нет\n")
        else:
            print(f"Найдено студентов с баллом > 4.0: {count}")

    print("Результаты сохранены в файл result.txt")

    print("\nСодержимое файла result.txt:")
    try:
        with open(RESULT_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            print(content if content else "Файл пуст")
    except Exception as e:
        print(f"Ошибка при чтении result.txt: {e}")

except Exception as e:
    print(f"Ошибка при записи в файл: {e}")

print("-" * 40)

if averages:
    max_avg = max(averages)
    print("СТУДЕНТ С НАИВЫСШИМ БАЛЛОМ:")

    found = False
    for i in range(len(students)):
        if averages[i] == max_avg:
            print(f"{students[i]} - {max_avg}")
            found = True

    if not found:
        print("Не найдено")
else:
    print("Нет данных о средних баллах")

print("Программа завершена!")