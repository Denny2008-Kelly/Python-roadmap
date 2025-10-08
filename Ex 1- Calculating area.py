import math

shape = input("What shape is it? ")

if shape.lower() == "rectangle":
    length = float(input("What is the length: "))
    width = float(input("What is the width: "))
    area = length * width
    print(f"The area is {area} m²")

elif shape.lower() == "circle":
    radius = float(input("What is the radius: "))
    area = math.pi * pow(radius, 2)
    print(f"The area is {round(area)} m²")

else:
    print("Sorry, I only know how to find the area of rectangles and circles.")
