from manimlib import *

class SquareToCircle(Scene):
  def construct(self):
    circle = Circle()
    circle.set_fill(BLUE, opacity=0.5)

    self.add(circle)
    