class List:

    def __init__(self):
        self._structure = [0] * 5

    def __getitem__(self, item):
        return self._structure[item]

    def __setitem__(self, key, value):
        self._structure[key] = value

    def append(self, value):
        self._structure[-1] = value

    def remove(self):
        del self._structure[0]

    def pop(self, value):
        del self._structure[value]
        return self._structure[value]

    def clear(self):
        self._structure = []

    def __str__(self):
        return f"({self._structure})"


a = List()

for i in a:
    print(i)
