class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50

    def eat(self):
        self.hunger -= 10
        self.energy += 5
        print(self.name, "ест")

    def sleep(self):
        self.energy += 10
        self.hunger += 5
        print(self.name, "спит")

    def status(self):
        print(self.name, "голод:", self.hunger, "энергия:", self.energy)


cat = Cat("Муся")

cat.status()
cat.eat()
cat.sleep()
cat.status()