from shapes import Circle, Rectangle, Triangle

def main():
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Rectangle.square(3),
        Triangle(3, 4),
    ]

    for shape in shapes:
        print(f"{shape}:")
        print(f"  Area: {shape.area()}")
        try:
            print(f"  Perimeter: {shape.perimeter()}")
        except NotImplementedError as e:
            print(f"  Perimeter: Not implemented ({e})")
        print()

if __name__ == "__main__":
    main()
