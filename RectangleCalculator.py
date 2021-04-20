import math
length = 214
width = 132
print("This rectangle is " + str(length) + " x " + str(width) + " Inches " )
if length == width:
  is_a_square = True
else:
  is_a_square = False 
print("Is this shape a square? " + str(is_a_square))
perimeter = length * 2 + width * 2 
print ("The perimiter is " + str(perimeter) + " Inches")
area = length * width
print ("The area is " + str(area) + " Inches")
length_of_diagonal = math.sqrt(int(length) * int(length) + int(width)*int(width))
print ("The length of the Diagonal is " + str(length_of_diagonal) + " Inches")
if length == width * 2 :
  Golden = True
else: 
  Golden = False 
print("Is this a Golden rectangle? : " + str(Golden))
