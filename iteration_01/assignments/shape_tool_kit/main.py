# TODO: Import classes from shapes.py (Rectangle, Circle, Triangle)
from shapes import Rectangle, Circle, Triangle
# TODO: Import helper functions from utils.py (e.g., cm2_to_m2, compare_areas)
from utils import cm2_to_m2, compare_areas
# TODO: Add a welcome() function (no return) that explains available shapes
# - Print available shapes and expected inputs
def welcome():
    print("Welcome to the Shape Tool Kit!")
    print("Available shapes:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")

# TODO: Implement interactive CLI to create shapes from user input
# - Ask user for shape type and its dimensions
# - Create the shape object and print area and describe()
def create_shape():
    shape_type = input("Enter the shape type: ")
    if shape_type == "Rectangle":
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        return Rectangle(width, height)
    elif shape_type == "Circle":
        radius = float(input("Enter the radius: "))
        return Circle(radius)
    elif shape_type == "Triangle":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        return Triangle(base, height)
    else:
        return None
# TODO (Optional Bonus): Allow dynamic multi-shape creation in one run
# - Let user choose multiple shapes and compare their areas
def compare_shapes():
    shape_a = create_shape()
    shape_b = create_shape()
    if shape_a is None or shape_b is None:
        print("Invalid shape type")
        return
    print(f"Shape A: {shape_a.describe()}")
    print(f"Shape B: {shape_b.describe()}")
    print(f"Shape A area: {shape_a.area()}")
    print(f"Shape B area: {shape_b.area()}")
    print(f"Shape A is {compare_areas(shape_a, shape_b)} than Shape B")
def main():
    welcome()
    shape = create_shape()
    shape.describe()
    compare_shapes()
if __name__ == "__main__":
    main()