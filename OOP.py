class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self._age = 0
        self.set_age(age)

    def make_sound(self):
        print("And some generic animal sound")

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print(f"Invalid age for {self.name}: age can't be negative.")

class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name, "Dog", age)
        self.breed = breed

    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self, name, favorite_toy, age):
        super().__init__(name, "Cat", age)
        self.favorite_toy = favorite_toy

    def make_sound(self):
        print("Meow!")

dog = Dog("Marsha", "Doge", 5)
cat = Cat("Pikachu", "Cat", 2)

print(f"{dog.name} is a {dog.breed} Labrador and is {dog.get_age()} years old.")
print(f"{cat.name} is a {cat.favorite_toy} who loves her Banana cat nip toy and is {cat.get_age()} years old.")

dog.set_age(5)
cat.set_age(-2)  

print("\nWho says what?")
animals = [dog, cat, Animal("Something", "Creature", 1)]
for a in animals:
    a.make_sound()
