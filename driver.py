# THE DRIVER PROGRAM TAKES INPUT FROM THE POST REQUEST QUERY GENERATED AND TRIGGERS ONE OF THE
# FUNCTIONS IN THE GRADIENT OR FIGURES FILE BASED ON THE ARGUMENTS RECEIVED.

from figures import DrawFigures
from gradients import Gradient


class Driver:
    def __init__(self, argument, size, color, gradient_scale, aa_scale):   # INI OF ALL ARGS
        self.argument = argument
        self.size = size
        self.color = color
        self.gradient_scale = gradient_scale
        self.aa_scale = aa_scale

    def draw_figure(self):
        draw1 = DrawFigures(self.size, self.aa_scale, self.color)
        if self.argument == "spread_circles_center":
            self.argument = "spread_circles"
            draw1.canvas(self.argument, 1)
        else:
            draw1.canvas(self.argument)

    def draw_gradient(self):
        gradient1 = Gradient(self.gradient_scale, self.size)
    
        if self.argument == "Gradient1":
            gradient1.canvas_one()

if __name__ == "__main__":
    print('goes')

    driver1 = Driver("circle", (1920, 1080), (125, 127, 128), 2, 4) 
    # let argument == Gradient
    if driver1.argument == "Gradient":
        driver1.draw_gradient()
    else:
        driver1.draw_figure()