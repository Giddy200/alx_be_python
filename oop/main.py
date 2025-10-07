from polymorphism_demo import Shape, Rectangle, Circle

def main():
    # Create a list containing instances of different derived classes
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Iterate through the list and call the 'area' method on each object.
    # The correct 'area' method is automatically called for each object type.
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()