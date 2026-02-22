class Animal:

    def __init__(self, name, age, weight):

        self.name = name
        self.age = age
        self.weight = weight

    def eat(self, food):

        self.weight += food
        return self.weight

    def info(self):

        print(f"{self.name}, {self.age} years, {self.weight} kg")


class Cat(Animal):


    def __init__(self, name, age, weight, breed):

        super().__init__(name, age, weight)
        self.breed = breed

    def bark(self):
        """Make cat sound."""
        print("MEOW!")



def demonstrate_classes():

    generic_animal = Animal("Generic", 5, 10)
    my_cat = Cat("Whiskers", 3, 4, "Siamese")


    generic_animal.info()
    my_cat.info()
    my_cat.bark()


    new_weight = my_cat.eat(0.5)
    print(f"Cat's new weight: {new_weight} kg")


if __name__ == "__main__":
    demonstrate_classes()
