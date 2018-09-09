from delegate import Person


class SubPerson:
    def __init__(self, name):
        self._person = Person.Person(name)

    def speak(self):
        print("SubPerson speak to you")
        self._person.speak()

    def run(self):
        print("SubPerson run with you")
        self._person.run()


### 使用委托模式实现 作为继承的替代模式 ###

if __name__ == '__main__':
    p = SubPerson("wang pen")
    p.speak()
    p.run()
