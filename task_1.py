def write_text_file(filename="text.txt"):
    lines = [
        "Привет, меня зовут Диана",
        "Я учусь в ТТИТ",
        "Мне 17 лет",
        "Я люблю книги",
        "Занимаюсь спортом"
    ]
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


def analyze_text_file(filename="text.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Сначала создадим его.")
        write_text_file(filename)
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

    lines = [line.rstrip("\n") for line in lines]

    num_lines = len(lines)

    num_words = 0
    for line in lines:
        words = line.split()
        num_words += len(words)

    longest_line = ""
    for line in lines:
        if len(line) > len(longest_line):
            longest_line = line

    print(f"Количество строк в файле: {num_lines}")
    print(f"Общее количество слов в файле: {num_words}")
    print(f"Самая длинная строка:\n{longest_line}")


def main():
    print("Задача 1:")
    write_text_file()
    analyze_text_file()


if __name__ == "__main__":
    main()
