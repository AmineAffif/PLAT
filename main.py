#importing libraries


# initialilasing the Point class
class Point:

    # basic point constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("I'm a constructed point")
        print("My x is : {}".format(self.x))
        print("My y is : {}".format(self.y))



# Get number of points
def getNumOfPoints():
    # Creating the list that handles all points
    global shape
    shape = list()
    # input the number of points
    global numOfPoints
    numOfPoints = int(input("Enter the number of fence post: "))
    while numOfPoints < 0:
        numOfPoints = numOfPoints = int(input("Enter the number of fence post: "))
    print("\n")

getNumOfPoints()

# Get X and Y position of each points
def getPointsPosition():
    for i in range(0, numOfPoints):
        print("Enter X position of the fence post {}".format(i+1))
        x = float(input(""))
        print("Enter Y position of the fence post {}".format(i+1))
        y = float(input(""))

        # insert point into the shape list
        shape.append(Point(x,y))
        print("I inserted a point")
        print("\n")

getPointsPosition()


    

# Display the area of the shape
print("------------------------------------------")

area = 0
for i in range(len(shape)-1):
        area += (shape[i].x * shape[i+1].y - shape[i+1].x * shape[i].y)/2
print("The area of the fence is : {}".format(abs(area)))

print("------------------------------------------")


# Display the center of gravity
x_center = 0
y_center = 0

for i in range(len(shape)-1):
        x_center += ((shape[i].x + shape[i+1].x) * (shape[i].x * shape[i+1].y - shape[i+1].x * shape[i].y)) * (1/6 * abs(area))
for i in range(len(shape)-1):
        y_center += ((shape[i].y + shape[i+1].y) * (shape[i].x * shape[i+1].y - shape[i+1].x * shape[i].y)) * (1/6 * abs(area))

print("Position du centre de gravité :")
print("X : " + format((abs(x_center))) )
print("Y : " + format((abs(y_center))) )


# Display if the cow is outside the fence or not