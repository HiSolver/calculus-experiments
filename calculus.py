from manimlib import *

class Tute1(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6,
        )

        graph = axes.get_graph(lambda x: x ** 2, x_range=[-2, 2, 1], color=YELLOW)
        rects = axes.get_riemann_rectangles(
            graph=graph, x_range=[-2, 2], dx=0.1, stroke_color=WHITE
        )

        graph2 = axes.get_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), t]),
            t_range=[-2 * PI, 2 * PI],
            color=RED,
        )

        self.add(axes, graph)
        self.wait()

        ##THE CAMERA IS AUTO SET TO PHI = 0 and THETA = -90

        self.move_camera(phi=60 * DEGREES)
        self.wait()
        self.move_camera(theta=-45 * DEGREES)

        self.begin_ambient_camera_rotation(
            rate=PI / 10, about="theta"
        )  # Rotates at a rate of radians per second
        self.wait()
        self.play(Create(rects), run_time=3)
        self.play(Create(graph2))
        self.wait()
        self.stop_ambient_camera_rotation()

        self.wait()
        self.begin_ambient_camera_rotation(
            rate=PI / 10, about="phi"
        )  # Rotates at a rate of radians per second
        self.wait(2)
        self.stop_ambient_camera_rotation()