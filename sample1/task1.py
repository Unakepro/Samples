class Dotter:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, other):
        newdot = Dotter(x=self._x + other._x, y=self._y + other._y, z=self._z + other._z)
        return newdot

    def __sub__(self, other):
        newdot = Dotter(x=self._x - other._x, y=self._y - other._y, z=self._z - other._z)
        return newdot

    def __truediv__(self, other):
        newdot = Dotter(x=self._x / other._x, y=self._y / other._y, z=self._z / other._z)
        return newdot

    def __mul__(self, other):
        newdot = Dotter(x=self._x * other._x, y=self._y * other._y, z=self._z * other._z)
        return newdot

    def un(self):
        return -self._x, -self._y, -self._z

    def __str__(self):
        return f"({self._x},{self._y},{self._z})"


dot1 = Dotter(1, 5, 8)
dot2 = Dotter(3, 6, 1)
dot3 = Dotter(6, 1, 1)
dot4 = Dotter(3, 1, 5)
dot5 = Dotter(2, 6, 1)
print(dot1 + dot2 + dot3 + dot4 + dot5)
print(dot1 - dot2 - dot3 - dot4 - dot5)
print(dot1 / dot2 / dot3 / dot4 / dot5)
print(dot1 * dot2 * dot3 * dot4 * dot5)
print(dot1.un())