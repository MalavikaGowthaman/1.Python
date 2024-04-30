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
    
class Multifunction():
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
    
#Create a class and function, and list out the items in the list
    def Subfields():
        items = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for sf in items:
            print(sf)

# odd or even
    def OddEven():
        num = int(input("Enter a number:"))
        if(num%2)==0:
            print(num, "is a even number")
        else:
            print(num, "is a odd number")
            return
        
# Create a function that tells elegibility of marriage 
    def percentage():

# getting user input
        Subject1= int(input("Subject1="))
        Subject2= int(input("Subject2="))
        Subject3= int(input("Subject3="))
        Subject4= int(input("Subject4="))
        Subject5= int(input("Subject5="))

#total marks
        Total = Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total: ", Total)
                
#total subjects
        Totalsubject = 5
                      
#percentage of marks
        percent = (Total / (Totalsubject * 100) *100)
        print("Percentage: ",percent)
        return 