import matplotlib.pyplot as plt


class Circle(object):

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius

    # Method
    def draw_circle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()


red_circle = Circle(10, "red")
red_circle.draw_circle()
print(dir(red_circle))

red_circle.add_radius(30)
red_circle.draw_circle()
