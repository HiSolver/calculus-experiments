%%manim -v WARNING -qm Paradox

class Paradox(Scene):
    def construct(self):

        axes = (
            Axes(
                x_range=[0, 10, 1],
                x_length=9,
                y_range=[0, 20, 5],
                y_length=6,
                axis_config={"include_numbers": True, "include_tip": False},
            )
            .to_edge(DL)
            .set_color(GREY)
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        func = axes.get_graph(
            lambda x: 0.1 * (x - 2) * (x - 5) * (x - 7) + 7, x_range=[0, 10], color=BLUE
        )

        x = ValueTracker(7)
        dx = ValueTracker(2)

        secant = always_redraw(
            lambda: axes.get_secant_slope_group(
                x=x.get_value(),
                graph=func,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label="dx",
                dy_label="dy",
                secant_line_color=GREEN,
                secant_line_length=8,
            )
        )
        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(x.get_value(), func.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(
                axes.c2p(
                    (x).get_value() + dx.get_value(),
                    func.underlying_function(x.get_value() + dx.get_value()),
                )
            )
        )

        self.add(axes, axes_labels, func)
        self.play(Create(VGroup(dot1, dot2, secant)))
        self.play(dx.animate.set_value(0.001), run_time=8)
        self.wait(2)
        self.play(x.animate.set_value(1), run_time=5)
        self.wait()
        self.play(x.animate.set_value(7), run_time=5)
        self.wait()
        self.play(dx.animate.set_value(2), run_time=6)
        self.wait()


%%manim -v WARNING -qm Costraints

class Costraints(ThreeDScene):
    def construct(self):
        
        resolution_fa = 42
        
        axes = ThreeDAxes()
        circle=Circle()
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        def param_curve(u, v):
            x = u
            y = v
            z = np.cos(u)*np.sin(v)+2
            return np.array([x, y, z])
        
        param_plane = Surface(
            param_curve,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-5, +5],
            u_range=[-2, +2]
        )
        
        param_plane.scale(1, about_point=ORIGIN)
        param_plane.set_style(fill_opacity=1,stroke_color=GREEN)
        param_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)axes = ThreeDAxes()
        self.add(axes,param_plane)
        
        self.move_camera(theta = -30 * DEGREES)
        self.wait(2)


%%manim -v WARNING -qm Costraints

class Costraints(ThreeDScene):
    def construct(self):
        
        resolution_fa = 42
        
        axes = ThreeDAxes()
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 0.4, [0.0, 0.0]
            d = np.linalg.norm(np.array([x - mu[0], y - mu[1]]))
            z = np.exp(-(d ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])
        
        def param_plane(u, v):
            x = u
            y = v
            z = 1
            return np.array([x, y, z])

        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, +2],
            u_range=[-2, +2]
        )
        
        tangent_plane = Surface(
            param_plane,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, +2],
            u_range=[-2, +2]
        )

        gauss_plane.scale(2, about_point=ORIGIN)
        gauss_plane.set_style(fill_opacity=1,stroke_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)
        
        tangent_plane.scale(2, about_point=ORIGIN)
        tangent_plane.set_style(fill_opacity=1,stroke_color=PURPLE)
        tangent_plane.set_fill_by_checkerboard(PURPLE, BLUE, opacity=0.5)
        
        axes = ThreeDAxes()
        
        self.add(axes, gauss_plane)
        self.add(axes, tangent_plane)