numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = [n * n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]


def generate_data(n):

    return [i * 2 for i in range(n) if i > 0]


def filter_multiples_of_ten(data):

    return [x for x in data if x % 10 == 0]

data = generate_data(100)
filtered_data = filter_multiples_of_ten(data)


def demonstrate_functionality():

    print("Original numbers:", numbers[:5], "...")
    print("Even squares:", even_squares[:5], "...")
    print("Odd numbers:", odd_numbers[:5], "...")
    print(f"Generated {len(data)} numbers")
    print(f"Multiples of 10: {filtered_data[:10]} ...")


if __name__ == "__main__":
    demonstrate_functionality()