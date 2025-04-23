from shape3d import Shape3D
from math import pi


class Cylinder(Shape3D):

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return round(2 * pi * self.radius * (self.radius + self.height), 2)

    def volume(self):
        return round(pi * self.height * (self.radius ** 2), 2)

    def __str__(self):
        return f"Cylinder with r={self.radius}, h={self.height}. S={self.surface_area()}, V={self.volume()}"