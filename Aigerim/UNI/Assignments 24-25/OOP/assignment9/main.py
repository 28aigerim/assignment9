from sphere import Sphere
from cylinder import Cylinder
from cube import Cube
import random


if __name__ == '__main__':

    def generate_shapes():
        shapes = []

        for _ in range(10):
            shape_type = random.choice(['Sphere', 'Cylinder', 'Cube'])

            if shape_type == 'Sphere':
                radius = random.randint(1, 10)
                shapes.append(Sphere(radius))
            elif shape_type == 'Cylinder':
                radius = random.randint(1, 10)
                height = random.randint(5, 20)
                shapes.append(Cylinder(radius, height))
            else:
                side = random.randint(1, 10)
                shapes.append(Cube(side))

        return shapes

    shapes = generate_shapes()
    for shape in shapes:
        print(shape)
