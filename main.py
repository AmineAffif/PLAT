class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    print("I'm a constructed point")
    print("My x is : {}".format(self.x))
    print("My y is : {}".format(self.y))

p1 = Point(2,9)