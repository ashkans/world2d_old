from manim import *

class MyAnimation(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.play(circle.animate.shift(2 * RIGHT))
        self.wait(1)
