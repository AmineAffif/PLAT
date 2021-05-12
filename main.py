#importing libraries
import re

# initialilasing the Point class
class Point:
    # basic point constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Je suis un piquet entre vos mains")
        print("Ma position X : {}".format(self.x))
        print("Ma position Y : {}".format(self.y))


# Get number of points
def getNumOfPoints():
    # Creating the list that handles all points
    global shape
    shape = list()
    # input the number of points
    global numOfPoints
    
    numOfPoints = input("Entrez le nombre de piquets : ")

    #contrôle de saisie regex (entier naturel positif)
    int_pattern = '^[0-9]+$'
    int_match = re.search(int_pattern, numOfPoints)
    # Tant que saisie invalide
    while int_match == None:
        print("Ecrivez un nombre valide")
        numOfPoints = input("Entrez le nombre de piquets : ")
        int_match = re.search(int_pattern, numOfPoints)
    
    print("Super ! On continue")
    print("\n")


# Get X and Y position of each points
def getPointsPosition():
    print("Si vous avez des nombres à virgule, utilisez un point")
    print("Exemple : 1.5")
    print("\n")

    #contrôle de saisie regex (entier naturel positif)
    float_pattern = '^(?=.)([+-]?([0-9]*)(\.([0-9]+))?)$'
    
    for i in range(0, int(numOfPoints)):
        
        # Saisie coordonée X
        print("Entrez la position X du piquet {}".format(i+1))
        x = input("")
        float_match = re.search(float_pattern, x)

        # Tant que saisie invalide
        while float_match == None:
            print("-- Ecrivez un nombre valide ! --")
            print("Entrez la position X du picket {}".format(i+1))
            x = input("")
            float_match = re.search(float_pattern, x)
            if (float_match != None):
                print("Bon. Continuons")

        x = float(x)

        # Saisie coordonée Y
        print("Entrez la position Y du piquet {}".format(i+1))
        y = input("")
        float_match = re.search(float_pattern, y)

        # Tant que saisie invalide
        while float_match == None:
            print("-- Ecrivez un nombre valide ! --")
            print("Entrez la position Y du piquet {}".format(i+1))
            y = input("")
            float_match = re.search(float_pattern, y)
            if (float_match != None):
                print("Bon. Continuons")

        y = float(y)

        # insert point into the shape list
        shape.append(Point(x,y))
        print("Piquet planté !")
        print("\n")


# Display the area of the shape
def getArea():
    print("------------------------------------------")

    global area
    area = 0
    for i in range(len(shape)-1):
            area += (shape[i].x * shape[i+1].y - shape[i+1].x * shape[i].y)/2
    print("L'aire est égale à : {}".format(abs(area)))

    print("------------------------------------------")


# Display the center of gravity
def getCenterGravity():
    print("------------------------------------------")
    global x_center
    global y_center

    x_center = 0
    y_center = 0

    for i in range(len(shape)-1):
            x_center += ((shape[i].x + shape[i+1].x) * (shape[i].x * shape[i+1].y - shape[i+1].x * shape[i].y)) * (1/6 * abs(area))
    for i in range(len(shape)-1):
            y_center += ((shape[i].y + shape[i+1].y) * (shape[i].x * shape[i+1].y - shape[i+1].x * shape[i].y)) * (1/6 * abs(area))

    print("Position du centre de gravité :")
    print("X : " + format((abs(x_center))) )
    print("Y : " + format((abs(y_center))) )

    print("------------------------------------------")


# Display if the cow is outside the fence or not


# Call all the functions
getNumOfPoints()
getPointsPosition()
getArea()
getCenterGravity()
