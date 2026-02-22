class UserData:


    def __init__(self, name, age):

        self.user_name = name
        self.age = age

    def print_info(self):

        print(f"User: {self.user_name}, Age: {self.age}")


def process_data(data_list):

    result = []
    for user_data in data_list:
        if user_data.age > 18:
            result.append(user_data.user_name.upper())
    return result