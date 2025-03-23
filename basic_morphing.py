from manim import *

class BasicMorphing(ThreeDScene):
    def construct(self):
        # Set camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create title
        title = Text("Minimal Morphosis").scale(0.7)
        title.to_corner(UL)
        title.set_color(WHITE)
        self.add(title)
        
        # Create just 8 spheres in a cube arrangement
        spheres = VGroup()
        for x in [-0.5, 0.5]:
            for y in [-0.5, 0.5]:
                for z in [-0.5, 0.5]:
                    sphere = Sphere(radius=0.2)
                    sphere.move_to([x, y, z])
                    sphere.set_color("#87CEEB")  # Sky blue
                    spheres.add(sphere)
        
        # Show spheres
        self.play(FadeIn(spheres), run_time=1)
        self.wait(1)
        
        # Rotate camera
        self.begin_ambient_camera_rotation(rate=0.15)
        
        # Create shape label
        shape_label = Text("").scale(0.6)
        shape_label.to_corner(DR)
        self.add(shape_label)
        
        # Current shape (starts as spheres)
        current_shape = spheres
        
        # Transform to tetrahedron
        new_label = Text("Tetrahedron").scale(0.6)
        new_label.to_corner(DR)
        new_label.set_color("#FF5252")
        self.play(Transform(shape_label, new_label))
        
        tetrahedron = Tetrahedron()
        tetrahedron.set_color("#FF5252")  # Red
        
        # Use FadeOut/FadeIn combination
        self.play(
            FadeOut(current_shape, run_time=1),
            FadeIn(tetrahedron, run_time=1),
        )
        current_shape = tetrahedron
        self.wait(1.5)
        
        # Transform to octahedron
        new_label = Text("Octahedron").scale(0.6)
        new_label.to_corner(DR)
        new_label.set_color("#FF9800")
        self.play(Transform(shape_label, new_label))
        
        octahedron = Octahedron()
        octahedron.set_color("#FF9800")  # Orange
        
        # Use FadeOut/FadeIn combination
        self.play(
            FadeOut(current_shape, run_time=1),
            FadeIn(octahedron, run_time=1),
        )
        current_shape = octahedron
        self.wait(1.5)
        
        # Transform to dodecahedron
        new_label = Text("Dodecahedron").scale(0.6)
        new_label.to_corner(DR)
        new_label.set_color("#FFEB3B")
        self.play(Transform(shape_label, new_label))
        
        dodecahedron = Dodecahedron()
        dodecahedron.set_color("#FFEB3B")  # Yellow
        
        # Use FadeOut/FadeIn combination
        self.play(
            FadeOut(current_shape, run_time=1),
            FadeIn(dodecahedron, run_time=1),
        )
        current_shape = dodecahedron
        self.wait(1.5)
        
        # Transform to icosahedron
        new_label = Text("Icosahedron").scale(0.6)
        new_label.to_corner(DR)
        new_label.set_color("#4CAF50")
        self.play(Transform(shape_label, new_label))
        
        icosahedron = Icosahedron()
        icosahedron.set_color("#4CAF50")  # Green
        
        # Use FadeOut/FadeIn combination
        self.play(
            FadeOut(current_shape, run_time=1),
            FadeIn(icosahedron, run_time=1),
        )
        current_shape = icosahedron
        self.wait(1.5)
        
        # Transform to large sphere
        new_label = Text("Sphere").scale(0.6)
        new_label.to_corner(DR)
        new_label.set_color("#00BCD4")
        self.play(Transform(shape_label, new_label))
        
        large_sphere = Sphere(radius=1)
        large_sphere.set_color("#00BCD4")  # Teal
        
        # Use FadeOut/FadeIn combination
        self.play(
            FadeOut(current_shape, run_time=1),
            FadeIn(large_sphere, run_time=1),
        )
        current_shape = large_sphere
        self.wait(1.5)
        
        # Transform to torus
        new_label = Text("Torus").scale(0.6)
        new_label.to_corner(DR)
        new_label.set_color("#7C4DFF")
        self.play(Transform(shape_label, new_label))
        
        torus = Torus()
        torus.set_color("#7C4DFF")  # Purple
        
        # Use FadeOut/FadeIn combination
        self.play(
            FadeOut(current_shape, run_time=1),
            FadeIn(torus, run_time=1),
        )
        current_shape = torus
        self.wait(1.5)
        
        # End
        self.stop_ambient_camera_rotation()
        
        # Fade out
        self.play(
            FadeOut(current_shape),
            FadeOut(shape_label),
            FadeOut(title),
            run_time=1.5
        )
        self.wait(1) 