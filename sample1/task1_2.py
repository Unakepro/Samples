class Quene:
    quene = []

    def __init__(self, add):
        self._add = add

    @classmethod
    def append(cls, add):
        cls.quene.append(add)

    @classmethod
    def pop(cls):
        return cls.quene.pop(0)


Quene.append(12)
Quene.append(15)
Quene.append(17)
print(Quene.pop())
