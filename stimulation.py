class Student:
    def __init__(self, name):
        self.name = name
        self.grade = 2

    def learn(self):
        self.grade += 3
        print(f"{self.name} учится и улучшает оценку!")

    def status(self):
        print(f"{self.name}: оценка = {self.grade}")


class Teacher:
    def __init__(self, name, student):
        self.name = name
        self.student = student

    def teach(self):
        print(f"{self.name} учит {self.student.name}")
        self.student.learn()


# --- симуляция ---
s1 = Student("Амина")
t1 = Teacher("Лейла", s1)

s1.status()
t1.teach()
s1.status()