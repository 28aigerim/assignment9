from shape3d import Shape3D
from math import pi


class Sphere(Shape3D):

    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return round(4 * pi * (self.radius ** 2), 2)

    def volume(self):
        return round((4/3) * pi * self.radius, 2)

    def __str__(self):
        return f'Sphere with radius {self.radius}. S={self.surface_area()}, V={self.volume()}'

