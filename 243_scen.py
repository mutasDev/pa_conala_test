#Call a base class's class method `do` from derived class `Derived`


class Base:
    def do(self):
        print("Doing something")

class Derived(Base):
    def do(self):
        super().do()
        print("Doing something else")