# initialilasing the Point class
class Point:

    # basic point constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("I'm a constructed point")
        print("My x is : {}".format(self.x))
        print("My y is : {}".format(self.y))

# Creating the list that handles all points
shape = []

# Get number of points
numOfPoints = int(input("Enter the number of fence post: "))
while numOfPoints < 0:
    numOfPoints = numOfPoints = int(input("Enter the number of fence post: "))

# Get X and Y position of each points
shape = list()

for i in range(0, numOfPoints):
    print("Enter X position of the fence post {}".format(i+1))
    x = float(input(""))
    print("Enter Y position of the fence post {}".format(i+1))
    y = float(input(""))

    # insert point into the shape list
    shape.append(Point(x,y))
    print("je rentre un point")

print("--------------------------------------------------")
print("--------------------------------------------------")
print("--------------------------------------------------")

for point in shape:
    print(point.x)
    

# Display the area of the shape

# Display the center of gravity

# Display if the cow is outside the fence or not