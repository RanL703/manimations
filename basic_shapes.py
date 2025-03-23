from manim import *

class BasicShapes(ThreeDScene):
    def construct(self):
        # Set camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create just 8 spheres in a cube arrangement
        spheres = VGroup()
        for x in [-0.5, 0.5]:
            for y in [-0.5, 0.5]:
                for z in [-0.5, 0.5]:
                    sphere = Sphere(radius=0.2)
                    sphere.move_to([x, y, z])
                    sphere.set_color(BLUE)
                    spheres.add(sphere)
        
        # Show spheres
        self.add(spheres)
        self.wait(1)
        
        # Rotate camera
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(1)
        
        # Create tetrahedron
        tetrahedron = Tetrahedron()
        tetrahedron.set_color(RED)
        
        # Use FadeOut and FadeIn instead of Transform
        self.play(
            FadeOut(spheres, run_time=1),
            FadeIn(tetrahedron, run_time=1),
        )
        self.wait(2)
        
        # End
        self.stop_ambient_camera_rotation()
        self.wait(1)
