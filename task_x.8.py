def validate_age(age):

    if 0 <= age <= 150:
        if age < 18:
            return "minor"
        if age < 65:
            return "adult"
        return "senior"
    return "invalid"


def check_increasing_sequence():
    x = 10
    y = 20
    z = 30

    if x < y < z:
        print("Increasing sequence")



if __name__ == "__main__":
    test_ages = [5, 25, 70, 200, -5]
    for test_age in test_ages:
        result = validate_age(test_age)
        print(f"Age {test_age}: {result}")

    check_increasing_sequence()
