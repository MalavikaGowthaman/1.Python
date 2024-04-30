#print area and perimeter of triangle using class and functions
# triangle.triangle()
# Height:32
# Breadth:34
# Area formula: (Height*Breadth)/2
# Area of Triangle: 544.0
# Height1:2
# Height2:4
# Breadth:4
# Perimeter formula: Height1+Height2+Breadth
# Perimeter of Triangle: 10
    
class triangle():
    def Area_triangle():

# getting input from users to find area of triangle
        Height = int(input("Height:"))
        Breadth = int(input("Breadth:"))

# Area of triangle
        Area_formula = (Height*Breadth)/2
        print("Area_formula : (Height*Breadth)/2")
        print("Area of Triangle: ",Area_formula)
        return 

# getting input from users to find perimeter of triangle
    def Perimeter_triangle():
        Height1 =int(input("Height1: "))
        Height2=int(input("Height2: "))
        Breadth=int(input("Breadth: "))

# perimeter of triangle
        Perimeter_formula= Height1+Height2+Breadth
        print("Perimeter_formula : Height1+Height2+Breadth")
        print("Perimeter of triangle: ",Perimeter_formula)
        return
    