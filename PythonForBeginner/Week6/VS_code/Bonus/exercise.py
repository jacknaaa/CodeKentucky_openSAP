import random
import math

# As for the additional challenge of using list comprehension, you can modify the calculate_pi function like this:
# def calculate_pi(num_points):
#     points_inside_circle = sum(1 for _ in range(num_points) if random.uniform(0, 1)**2 + random.uniform(0, 1)**2 < 1)
#     calculated_pi = 4 * (points_inside_circle / num_points)
#     return calculated_pi


def calculate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x**2 + y**2 < 1:
            points_inside_circle += 1

    calculated_pi = 4 * (points_inside_circle / num_points)
    return calculated_pi


def main():
    num_points = 10000

    calculated_pi = calculate_pi(num_points)
    math_pi = math.pi

    print(f"Calculated value of π: {calculated_pi:.4f}")
    print(f"Value of π from math library: {math_pi}")
    print(f"Difference: {calculated_pi - math_pi:.16f}")


if __name__ == "__main__":
    main()
