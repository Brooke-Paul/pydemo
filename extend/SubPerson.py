from extend.Person import Person


class SubPerson(Person):
    def __init__(self, name):
        self.name = name
        print("SubPerson __init__")

    def speak(self):
        print("SubPerson speak to you")
        super().speak()

    def run(self):
        print("SubPerson run with you")
        super().run()


### 使用继承模式实现 ###

if __name__ == '__main__':
    s = Person("wang gang")
    p = SubPerson("wang pen")
    p.speak()
    p.run()
