class MyContextManager:

    def __init__(self, name, mode, text):
        self._name = name
        self._mode = mode
        self._text = text

    def __enter__(self):
        return self._name, self._mode, self._text

    def write(self):
        with open(self._name, mode=self._mode) as file:
            file.write(self._text)

    def __exit__(self, *args):
        self._name = None
        self._mode = None
        self._text = None


with MyContextManager("file", 'w', "hello"):
    MyContextManager("file", 'w', "hello").write()
