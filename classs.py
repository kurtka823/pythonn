class Mother:
    eye_color = "зелёные"

    def cook(self):
        print("Умеет готовить")

class Father:
    height = "высокий"

    def work(self):
        print("Работает")

class Child(Mother, Father):
    def info(self):
        print("Глаза:", self.eye_color)
        print("Рост:", self.height)


child = Child()

child.info()
child.cook()
child.work()