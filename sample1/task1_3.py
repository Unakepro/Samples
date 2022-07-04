class Steck:
    steck = []

    def __init__(self, add):
        self._add = add

    @classmethod
    def append(cls, add):
        cls.steck.append(add)

    @classmethod
    def take(cls):
        return cls.steck[-1]


Steck.append(35)
Steck.append("de")
Steck.append(32)
print(Steck.take())
