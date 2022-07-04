import abc
from datetime import date


class Person(abc.ABC):
    my_list = []

    def __init__(self, lname, birthday, faculty):
        self._lname = lname
        self._birthday = birthday
        self._faculty = faculty

    @abc.abstractmethod
    def set(self, lname, birthday, faculty):
        self._lname = lname
        self._birthday = birthday
        self._faculty = faculty

    @abc.abstractmethod
    def get(self):
        return self._lname, self._birthday, self._faculty

    @abc.abstractmethod
    def bir(self):
        today = date.today()
        return today.year - self._birthday[0] - ((today.month, today.day) < (self._birthday[1], self._birthday[2]))

    @abc.abstractmethod
    def append(self):
        Person.my_list.append(self)


class Abiturient(Person):
    def set(self, lname, birthday, faculty):
        self._lname = lname
        self._birthday = birthday
        self._faculty = faculty

    def get(self):
        return self._lname, self._birthday, self._faculty

    def bir(self):
        today = date.today()
        return today.year - self._birthday[0] - ((today.month, today.day) < (self._birthday[1], self._birthday[2]))

    def append(self):
        Person.my_list.append(self)


class Student(Person):

    def __init__(self, lname, birthday, faculty, course):
        super().__init__(lname, birthday, faculty)
        self._course = course

    def set(self, lname, birthday, faculty, course):
        self._lname = lname
        self._birthday = birthday
        self._faculty = faculty
        self._course = course

    def get(self):
        return self._lname, self._birthday, self._faculty, self._course

    def bir(self):
        today = date.today()
        return today.year - self._birthday[0] - ((today.month, today.day) < (self._birthday[1], self._birthday[2]))

    def append(self):
        Person.my_list.append(self)


class Teacher(Person):
    def __init__(self, lname, birthday, faculty, course, experience):
        super().__init__(lname, birthday, faculty)
        self._course = course
        self._experience = experience

    def set(self, lname, birthday, faculty, course, experience):
        self._lname = lname
        self._birthday = birthday
        self._faculty = faculty
        self._course = course
        self._experience = experience

    def get(self):
        return self._lname, self._birthday, self._faculty, self._course, self._faculty, self._experience

    def bir(self):
        today = date.today()
        return today.year - self._birthday[0] - ((today.month, today.day) < (self._birthday[1], self._birthday[2]))

    def append(self):
        Person.my_list.append(self)


ark = Abiturient("Grisha", [1980, 1, 10], "Programming")
ark1 = Student("Andrey", [2000, 2, 12], "Programming", "Python")
ark2 = Teacher("Krimson", [1910, 23, 9], "Security", "C++", "5 years")


ark.append()
ark1.append()
ark2.append()


for i in Person.my_list:
    print(i.get())
    if i.bir() > 42:
        print(f"{i.get()[0]} is older than 42")
