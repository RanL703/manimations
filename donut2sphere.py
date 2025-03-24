from manim import *

class DonutToSphere(ThreeDScene):
    def construct(self):
        donut = Torus(major_radius=2, minor_radius=1, fill_opacity=0.5, color=BLUE)
        sphere = Sphere(radius=2, fill_opacity=0.5, color=RED)
        self.set_camera_orientation(phi=75 * DEGREES, theta =- 45 * DEGREES)
        self.play(Create(donut))
        self.wait()
        self.play(Transform(donut, sphere))
        self.wait()