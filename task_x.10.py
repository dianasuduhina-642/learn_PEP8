import time

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper


@timer
def heavy_computation(n):

    return sum(i * i for i in range(n))


def demonstrate_functional_operations():

    numbers = [1, 2, 3, 4, 5]

    squared_numbers = list(map(lambda x: x * x, numbers))
    print(f"Original numbers: {numbers}")
    print(f"Squared numbers: {squared_numbers}")

    filtered_numbers = list(filter(lambda x: x > 10, squared_numbers))
    print(f"Filtered numbers (>10): {filtered_numbers}")

    return squared_numbers, filtered_numbers


def main():

    print("=== Heavy Computation Demo ===")
    for n in [10, 100, 1000, 10000]:
        result = heavy_computation(n)
        print(f"Sum of squares for n={n}: {result}")
        print("-" * 40)

    print("\n=== Functional Operations Demo ===")
    squared, filtered = demonstrate_functional_operations()

    print(f"\nFinal results:")
    print(f"Squared: {squared}")
    print(f"Filtered: {filtered}")


if __name__ == "__main__":
    main()