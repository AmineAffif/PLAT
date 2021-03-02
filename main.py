# initialilasing the Point class
class Point:
    # basic point constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Je suis un picket entre vos mains")
        print("Ma position X : {}".format(self.x))
        print("Ma position Y : {}".format(self.y))


# Get number of points
def getNumOfPoints():
    # Creating the list that handles all points
    global shape
    shape = list()
    # input the number of points
    global numOfPoints
    numOfPoints = int(input("Entrez le nombre de pickets : "))
    while numOfPoints < 0:
        numOfPoints = numOfPoints = int(input("Entrez le nombre de pickets : "))
    print("\n")


# Get X and Y position of each points
def getPointsPosition():
    for i in range(0, numOfPoints):
        print("Entrez la position X du picket {}".format(i+1))
        x = float(input(""))
        print("Entrez la position Y du picket {}".format(i+1))
        y = float(input(""))

        # insert point into the shape list
        shape.append(Point(x,y))
        print("Picket planté !")
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
