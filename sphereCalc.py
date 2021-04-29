import math
diameter = 10;
diameter = input("What's the Diamater? ")
raduis = int(diameter) // 2
circumference = 2 * math.pi * int(raduis)
area = 4* math.pi * int(raduis) ** 2
volume = 4/3 * math.pi * int(raduis)** 3
print("Diameter: %7s " % diameter + "     Inches")
print("Radius: %8d " % raduis + "      Inches")
print("Circumference: %5.2f " % circumference + "  Inches")
print("Area: %15.2f " % area + " Square Inches")
print("Volume: %13.2f " % volume + " Cubic Inches")
