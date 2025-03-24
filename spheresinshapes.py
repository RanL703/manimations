from manim import *
import numpy as np
import cmath
from colour import Color  # Add explicit import for Color

class ComplexFunctionVisualization(ThreeDScene):
    def construct(self):
        # Disable caching to improve performance with many objects
        config.disable_caching = True
        
        # Title for the visualization
        title = Text("Complex Function Integration Visualization", font_size=42).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Set initial camera position
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        
        # Setup the scene with explanatory text
        self.setup_axes()
        
        # Introduction text
        intro_text = Text(
            "Visualizing complex functions and their integration paths in 3D space",
            font_size=24
        ).next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(intro_text)
        self.play(Write(intro_text))
        self.wait(1)
        
        # Remove intro text after showing it
        self.play(FadeOut(intro_text))
        
        # Define complex functions to visualize with descriptions
        functions = [
            (lambda z: z**2, "f(z) = z²", "Simple quadratic function"),
            (lambda z: z**3, "f(z) = z³", "Cubic function"),
            (lambda z: 1/z if z != 0 else float('inf'), "f(z) = 1/z", "Function with singularity at z=0"),
        ]
        
        # Define integration paths with descriptions
        paths = [
            self.create_circular_path(center=0, radius=2, name="Circle |z| = 2", 
                                      description="Circular path of radius 2 around origin"),
            self.create_rectangular_path(-2, -2, 2, 2, name="Rectangle around origin", 
                                         description="Rectangular path enclosing the origin"),
            self.create_custom_path([(-2, -2), (2, -2), (2, 2), (0, 0), (-2, 2), (-2, -2)], 
                                    name="Custom path", 
                                    description="Custom path with multiple segments")
        ]
        
        # Legend for color interpretation
        self.show_color_legend()
        
        # Visualize each function with integration paths
        for func, func_name, func_desc in functions[:2]:  # Use fewer functions for performance
            # Create and show the complex function visualization
            surface, grid_spheres = self.visualize_complex_function(func, func_name)
            
            # Show function name and description
            func_text = Text(func_name, font_size=36).to_corner(UL)
            func_desc_text = Text(func_desc, font_size=24).next_to(func_text, DOWN).to_edge(LEFT)
            self.add_fixed_in_frame_mobjects(func_text, func_desc_text)
            
            # Animation to display the function
            self.play(
                FadeIn(surface),
                FadeIn(grid_spheres),
                Write(func_text),
                Write(func_desc_text)
            )
            
            # Add explanatory text about the visualization
            viz_explanation = Text(
                "Height (z-axis) = |f(z)| (magnitude)",
                font_size=20
            ).to_edge(DOWN).shift(UP * 0.5)
            color_explanation = Text(
                "Color = arg(f(z)) (phase)",
                font_size=20
            ).next_to(viz_explanation, DOWN)
            
            self.add_fixed_in_frame_mobjects(viz_explanation, color_explanation)
            self.play(
                Write(viz_explanation),
                Write(color_explanation)
            )
            self.wait(1)
            
            # For each function, demonstrate at least one integration path
            path_idx = functions.index((func, func_name, func_desc)) % len(paths)
            path, path_name, path_desc = paths[path_idx]
            
            # Remove previous explanations
            self.play(
                FadeOut(viz_explanation),
                FadeOut(color_explanation)
            )
            
            # Show path name and description
            path_text = Text(f"Path: {path_name}", font_size=28).next_to(func_desc_text, DOWN).to_edge(LEFT)
            path_desc_text = Text(path_desc, font_size=20).next_to(path_text, DOWN).to_edge(LEFT)
            self.add_fixed_in_frame_mobjects(path_text, path_desc_text)
            self.play(
                Write(path_text),
                Write(path_desc_text)
            )
            
            # Explanation of integration
            integration_explanation = Text(
                "Integrating along the path: watch the accumulation",
                font_size=24
            ).to_edge(DOWN).shift(UP * 0.5)
            self.add_fixed_in_frame_mobjects(integration_explanation)
            self.play(Write(integration_explanation))
            
            # Visualize integration with educational elements
            result_text = self.visualize_integration_educational(func, path, grid_spheres)
            self.add_fixed_in_frame_mobjects(result_text)
            
            # Add explanation of the result
            if abs(complex(result_text.tex_string.split("=")[1])) < 0.5:
                result_explanation = Text(
                    "Result ≈ 0: Confirms Cauchy's Integral Theorem for analytic functions",
                    font_size=20
                ).to_edge(DOWN)
            else:
                result_explanation = Text(
                    "Non-zero result: Path encloses singularities or branch points",
                    font_size=20
                ).to_edge(DOWN)
                
            self.add_fixed_in_frame_mobjects(result_explanation)
            self.play(Write(result_explanation))
            
            # Move camera to view the scene from different angles with explanation
            camera_move_text = Text(
                "Moving camera to view from different angle",
                font_size=24
            ).to_edge(DOWN)
            self.add_fixed_in_frame_mobjects(camera_move_text)
            self.play(
                FadeOut(integration_explanation),
                FadeOut(result_explanation),
                Write(camera_move_text)
            )
            
            self.move_camera(
                theta=-90 * DEGREES,
                run_time=3,
                about_point=ORIGIN
            )
            self.wait(1)
            
            # Clean up for next function
            self.play(
                FadeOut(surface),
                FadeOut(grid_spheres),
                FadeOut(func_text),
                FadeOut(func_desc_text),
                FadeOut(path_text),
                FadeOut(path_desc_text),
                FadeOut(camera_move_text),
                FadeOut(result_text)
            )
        
        # Closing title
        closing_title = Text("Complex Analysis: Visualizing Integration", font_size=42).to_edge(UP)
        closing_text = Text(
            "Complex integration is a powerful tool in mathematics and physics",
            font_size=24
        ).next_to(closing_title, DOWN)
        
        self.add_fixed_in_frame_mobjects(closing_title, closing_text)
        self.play(
            ReplacementTransform(title, closing_title),
            Write(closing_text)
        )
        self.wait(2)
    
    def show_color_legend(self):
        # Create a color legend to explain phase mapping
        legend_title = Text("Color Legend: Phase Mapping", font_size=24).to_corner(UR)
        
        # Create a color wheel for the legend
        radius = 0.3
        color_wheel = VGroup()
        num_segments = 12
        for i in range(num_segments):
            angle_start = i * 2 * PI / num_segments
            angle_end = (i + 1) * 2 * PI / num_segments
            phase = (angle_start + angle_end) / 2 - PI
            color = self.phase_to_color(phase)
            
            segment = AnnularSector(
                inner_radius=0,
                outer_radius=radius,
                angle=2 * PI / num_segments,
                start_angle=angle_start,
                color=color,
                fill_opacity=1
            )
            color_wheel.add(segment)
        
        # Add labels
        phase_labels = VGroup()
        label_points = [0, PI/2, PI, 3*PI/2]
        label_texts = ["0", "π/2", "π", "3π/2"]
        
        for angle, text in zip(label_points, label_texts):
            label = Text(text, font_size=16)
            label.move_to(radius * 1.3 * np.array([np.cos(angle), np.sin(angle), 0]))
            phase_labels.add(label)
        
        # Group everything
        legend = VGroup(color_wheel, phase_labels)
        legend.next_to(legend_title, DOWN, buff=0.2)
        legend.to_corner(UR)
        
        # Add to scene
        self.add_fixed_in_frame_mobjects(legend_title, legend)
        self.play(
            Write(legend_title),
            FadeIn(legend)
        )
        
    def setup_axes(self):
        # Create and add axes
        axes = ThreeDAxes(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            z_range=(-2, 5, 1),
            x_length=10,
            y_length=10,
            z_length=7
        )
        
        # Labels with more descriptive text - moved to fixed frame (2D) positions
        x_label = Text("Real Axis (Re(z))", font_size=24).to_corner(DR).shift(UP * 1.5 + LEFT * 3)
        y_label = Text("Imaginary Axis (Im(z))", font_size=24).to_corner(DL).shift(UP * 1.5 + RIGHT * 3)
        z_label = Text("Magnitude (|f(z)|)", font_size=24).to_corner(UL).shift(DOWN * 1.5 + RIGHT * 3)
        
        # Add a complex plane (xy-plane) with grid lines
        complex_plane = NumberPlane(
            x_range=(-5, 5),
            y_range=(-5, 5),
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        ).shift(IN * 0.01)  # Slight offset to avoid z-fighting
        
        # Add axis labels
        self.add(axes, complex_plane)
        self.add_fixed_in_frame_mobjects(x_label, y_label, z_label)
        
        # Add explanatory text about the coordinate system
        coord_explanation = Text(
            "The complex plane is represented by the x-y plane",
            font_size=24
        ).to_edge(DOWN)
        
        self.add_fixed_in_frame_mobjects(coord_explanation)
        self.play(Write(coord_explanation))
        self.wait(1)
        self.play(FadeOut(coord_explanation))
    
    def visualize_complex_function(self, func, func_name):
        # Parameters for the grid - REDUCED for better performance
        grid_size = 12  # Reduced from 20
        x_range = np.linspace(-3, 3, grid_size)
        y_range = np.linspace(-3, 3, grid_size)
        sphere_radius = 0.08  # Slightly larger for better visibility with fewer points
        
        # Create a group for the spheres
        grid_spheres = VGroup()
        
        # Create surface points for the function
        surface_points = []
        
        # Animation to show building the surface point by point
        building_text = Text("Building the complex function visualization...", font_size=24).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(building_text)
        self.play(Write(building_text))
        
        # Create preview sphere to demonstrate what we're doing
        preview_sphere = None
        preview_position = None
        
        # Sample points to create the surface
        for x_idx, x in enumerate(x_range):
            row_points = []
            for y_idx, y in enumerate(y_range):
                z = complex(x, y)
                try:
                    w = func(z)
                    # If w is infinity or NaN, skip this point
                    if w == float('inf') or w != w:
                        continue
                    
                    # Extract magnitude and phase
                    magnitude = abs(w)
                    phase = cmath.phase(w)
                    
                    # Cap extremely large values
                    if magnitude > 5:
                        magnitude = 5
                    
                    # Color based on phase (hue)
                    color = self.phase_to_color(phase)
                    
                    # Create sphere at (x, y, |w|)
                    sphere = Sphere(
                        radius=sphere_radius,
                        fill_opacity=0.8,
                        color=color,
                        resolution=(8, 8)  # Lower resolution for better performance
                    ).move_to(np.array([x, y, magnitude]))
                    
                    # For visualization, show a few spheres being placed
                    if preview_sphere is None and x_idx % 3 == 0 and y_idx % 3 == 0:
                        preview_sphere = sphere.copy()
                        preview_position = np.array([x, y, magnitude])
                        preview_text = MathTex(
                            f"f({x:.1f} + {y:.1f}i) = {w.real:.1f} + {w.imag:.1f}i",
                            font_size=24
                        ).to_edge(DOWN).shift(UP * 0.5)
                        magnitude_text = Text(
                            f"|f(z)| = {magnitude:.2f}, arg(f(z)) = {phase:.2f}",
                            font_size=20
                        ).next_to(preview_text, DOWN)
                        
                        self.add_fixed_in_frame_mobjects(preview_text, magnitude_text)
                        self.play(
                            FadeOut(building_text),
                            FadeIn(preview_sphere),
                            Write(preview_text),
                            Write(magnitude_text)
                        )
                        
                        # Show connection between complex plane and height
                        plane_dot = Dot(np.array([x, y, 0]), color=RED)
                        height_line = Line(
                            np.array([x, y, 0]),
                            np.array([x, y, magnitude]),
                            color=YELLOW
                        )
                        self.play(
                            FadeIn(plane_dot),
                            Create(height_line)
                        )
                        self.wait(1)
                        self.play(
                            FadeOut(plane_dot),
                            FadeOut(height_line),
                            FadeOut(preview_text),
                            FadeOut(magnitude_text),
                            FadeOut(preview_sphere)
                        )
                    
                    grid_spheres.add(sphere)
                    row_points.append([x, y, magnitude])
                except:
                    # Skip points where function cannot be evaluated
                    pass
            if row_points:
                surface_points.append(row_points)
        
        # Create a surface
        surface = None
        if len(surface_points) > 1 and all(len(row) > 1 for row in surface_points):
            # Ensure we have enough points with consistent row lengths
            min_row_length = min(len(row) for row in surface_points)
            surface_points = [row[:min_row_length] for row in surface_points]
            
            # Create the surface with appropriate coloring
            surface = Surface(
                lambda u, v: np.array([
                    surface_points[int(u * (len(surface_points) - 1))][int(v * (min_row_length - 1))][0],
                    surface_points[int(u * (len(surface_points) - 1))][int(v * (min_row_length - 1))][1],
                    surface_points[int(u * (len(surface_points) - 1))][int(v * (min_row_length - 1))][2]
                ]),
                u_range=[0, 1],
                v_range=[0, 1],
                resolution=(len(surface_points), min_row_length),
                fill_opacity=0.6,
                stroke_opacity=0.4,
                stroke_width=0.5,
            )
            
            # Apply color gradient based on height
            surface.set_fill_by_value(
                axes=ThreeDAxes(),
                colors=[(BLUE_E, -1), (GREEN, 0), (YELLOW, 2), (RED, 4)],
                axis=2
            )
        
        return surface, grid_spheres
    
    def phase_to_color(self, phase):
        # Convert phase to color using HSL color space
        # Map phase from [-π, π] to [0, 1] for hue
        hue = (phase + np.pi) / (2 * np.pi)
        return Color(hsl=(hue, 0.8, 0.6))
    
    def create_circular_path(self, center=0, radius=1, name="Circle", description=""):
        # Create a circular path in the complex plane
        center_x, center_y = (center.real, center.imag) if isinstance(center, complex) else (center, 0)
        circle = Circle(
            radius=radius,
            color=WHITE,
            stroke_width=4
        ).shift(np.array([center_x, center_y, 0.01]))  # Slight z-offset to be visible
        
        return circle, name, description
    
    def create_rectangular_path(self, x1, y1, x2, y2, name="Rectangle", description=""):
        # Create a rectangular path in the complex plane
        vertices = [
            np.array([x1, y1, 0.01]),
            np.array([x2, y1, 0.01]),
            np.array([x2, y2, 0.01]),
            np.array([x1, y2, 0.01]),
            np.array([x1, y1, 0.01]),
        ]
        
        path = VMobject(color=WHITE, stroke_width=4)
        path.set_points_as_corners(vertices)
        
        return path, name, description
    
    def create_custom_path(self, points, name="Custom Path", description=""):
        # Create a custom path from a list of points
        vertices = [np.array([x, y, 0.01]) for x, y in points]
        
        path = VMobject(color=WHITE, stroke_width=4)
        path.set_points_as_corners(vertices)
        
        return path, name, description
    
    def visualize_integration_educational(self, func, path_tuple, grid_spheres):
        path, path_name, path_desc = path_tuple
        
        # Show the path with explanation
        path_explanation = Text(
            "This path defines our contour of integration", 
            font_size=20
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(path_explanation)
        
        self.play(
            Create(path),
            Write(path_explanation)
        )
        self.wait(1)
        
        # Create a dot to move along the path
        moving_dot = Sphere(radius=0.1, color=YELLOW, resolution=(8, 8)).move_to(path.get_start())
        dot_explanation = Text(
            "The yellow sphere moves along the integration path", 
            font_size=20
        ).next_to(path_explanation, DOWN)
        self.add_fixed_in_frame_mobjects(dot_explanation)
        
        self.play(
            FadeIn(moving_dot),
            Write(dot_explanation),
            FadeOut(path_explanation)
        )
        
        # Initialize integral value
        integral_value = 0
        integral_text = MathTex(
            r"\int_C f(z) \, dz = 0",
            font_size=32
        ).to_corner(UR)
        
        integral_explanation = Text(
            "The integral accumulates as we move along the path",
            font_size=20
        ).next_to(dot_explanation, DOWN)
        self.add_fixed_in_frame_mobjects(integral_text, integral_explanation)
        
        self.play(
            Write(integral_text),
            Write(integral_explanation)
        )
        
        # Ensure all previous explanations are removed
        self.play(
            FadeOut(dot_explanation), 
            FadeOut(integral_explanation)
        )
        
        # Discretize the path for integration
        points = path.get_points()
        # Take fewer points for better performance
        path_points = [points[i] for i in range(0, len(points), 6)]  # Increased step from 3 to 6
        
        # Add dots to show the discretization
        discretization_dots = VGroup()
        for point in path_points:
            dot = Dot(point, color=BLUE, radius=0.05)
            discretization_dots.add(dot)
        
        discretization_explanation = Text(
            "We discretize the path into small segments for numerical integration",
            font_size=20
        ).to_edge(DOWN)
        
        self.add_fixed_in_frame_mobjects(discretization_explanation)
        self.play(
            FadeIn(discretization_dots),
            Write(discretization_explanation)
        )
        self.wait(1)
        
        self.play(
            FadeOut(discretization_dots),
            FadeOut(discretization_explanation)
        )
        
        # Add trapezoidal rule explanation
        trap_explanation = Text(
            "Using the trapezoidal rule: ∫f(z)dz ≈ Σ[f(z₁) + f(z₂)]/2 · Δz",
            font_size=20
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(trap_explanation)
        
        self.play(Write(trap_explanation))
        self.wait(1)
        
        # Calculate integral value first without animation to avoid lag
        integral_values = [0]
        
        for i in range(1, len(path_points)):
            current_point = path_points[i-1]
            next_point = path_points[i]
            
            z1 = complex(current_point[0], current_point[1])
            z2 = complex(next_point[0], next_point[1])
            
            dz = z2 - z1
            try:
                f_z1 = func(z1) if z1 != 0 or "1/z" not in str(func) else float('inf')
                f_z2 = func(z2) if z2 != 0 or "1/z" not in str(func) else float('inf')
                
                if f_z1 != float('inf') and f_z2 != float('inf'):
                    segment_integral = 0.5 * (f_z1 + f_z2) * dz
                    integral_values.append(integral_values[-1] + segment_integral)
                else:
                    integral_values.append(integral_values[-1])
            except:
                integral_values.append(integral_values[-1])
        
        # Remove trapezoidal rule explanation
        self.play(FadeOut(trap_explanation))
        
        # Now animate with pre-calculated values
        progress_explanation = Text(
            "Watching the integral accumulate as we travel along the path",
            font_size=20
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(progress_explanation)
        self.play(Write(progress_explanation))
        
        # Keep track of any active point contribution text
        active_point_contribution = None
        
        for i in range(1, len(path_points)):
            # Get current and next point
            current_point = path_points[i-1]
            next_point = path_points[i]
            integral_value = integral_values[i]
            
            # Create the segment for this step
            segment = Line(current_point, next_point, color=YELLOW, stroke_width=5)
            segment_label = MathTex(r"\Delta z_{" + str(i) + "}", font_size=16).next_to(segment, UP, buff=0.1)
            
            # Update moving dot
            self.play(
                Create(segment),
                Write(segment_label),
                moving_dot.animate.move_to(next_point),
                run_time=0.5
            )
            
            # Only highlight a few spheres to improve performance
            if i % 2 == 0:  # Only highlight every other point
                highlighted = False
                # Limit number of spheres to check
                for sphere in grid_spheres[:30]:  # Check only first 30 spheres
                    sphere_pos = sphere.get_center()
                    distance = np.sqrt((sphere_pos[0] - next_point[0])**2 + (sphere_pos[1] - next_point[1])**2)
                    if distance < 0.5:
                        # Highlight the sphere and show its value
                        z_val = complex(next_point[0], next_point[1])
                        try:
                            w_val = func(z_val)
                            if w_val != float('inf') and w_val == w_val:
                                # Clean up previous contribution text if it exists
                                if active_point_contribution:
                                    self.play(FadeOut(active_point_contribution), run_time=0.1)
                                
                                point_contribution = Text(
                                    f"f({z_val.real:.1f} + {z_val.imag:.1f}i) contributes",
                                    font_size=16
                                ).next_to(progress_explanation, DOWN)
                                active_point_contribution = point_contribution
                                
                                self.add_fixed_in_frame_mobjects(point_contribution)
                                
                                self.play(
                                    Flash(sphere, color=WHITE, flash_radius=0.2, line_length=0.1),
                                    Write(point_contribution),
                                    run_time=0.3
                                )
                                highlighted = True
                                break  # Just highlight one sphere at each step
                        except:
                            pass
                
                # Update integral text, but less frequently
                if highlighted or i % 4 == 0:
                    new_integral_text = MathTex(
                        r"\int_C f(z) \, dz = " + f"{integral_value:.2f}",
                        font_size=32
                    ).to_corner(UR)
                    self.play(
                        ReplacementTransform(integral_text, new_integral_text),
                        run_time=0.3
                    )
                    integral_text = new_integral_text
            
            # Clean up segment after we're done with it
            self.play(
                FadeOut(segment),
                FadeOut(segment_label),
                run_time=0.2
            )
        
        # Clean up any remaining point contribution text
        if active_point_contribution:
            self.play(FadeOut(active_point_contribution), run_time=0.1)
        
        # Final result with educational explanation
        final_result = MathTex(
            r"\oint_C f(z) \, dz = " + f"{integral_value:.2f}",
            font_size=36
        ).to_corner(DR)
        
        final_explanation = Text(
            "The symbol ∮ indicates integration around a closed curve",
            font_size=20
        ).to_edge(DOWN)
        
        self.play(
            FadeOut(progress_explanation),
            Transform(integral_text, final_result),
            Write(final_explanation),
            run_time=1
        )
        
        # If integral is close to zero, explain Cauchy's theorem
        if abs(integral_value) < 0.5:
            cauchy_explanation = Text(
                "Result ≈ 0: Consistent with Cauchy's Integral Theorem!",
                font_size=24,
                color=GREEN
            ).next_to(final_explanation, DOWN)
            self.add_fixed_in_frame_mobjects(cauchy_explanation)
            self.play(Write(cauchy_explanation))
            self.wait(1)
            self.play(
                FadeOut(final_explanation),
                FadeOut(cauchy_explanation)
            )
        else:
            # It's probably the 1/z function
            residue_explanation = Text(
                "Non-zero result: Path encircles a singularity (pole)",
                font_size=24,
                color=YELLOW
            ).next_to(final_explanation, DOWN)
            self.add_fixed_in_frame_mobjects(residue_explanation)
            self.play(Write(residue_explanation))
            self.wait(1)
            self.play(
                FadeOut(final_explanation),
                FadeOut(residue_explanation)
            )
        
        # Clean up
        self.play(FadeOut(moving_dot))
        
        return final_result


class CubeOfSpheres(ThreeDScene):
    def construct(self):
        # Disable caching to improve performance with many objects
        config.disable_caching = True
        
        # Add title
        title = Text("3D Cube of Spheres Visualization", font_size=42).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Add description
        description = Text(
            "A simple 3D arrangement of spheres in a cubic lattice",
            font_size=24
        ).next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(description)
        self.play(Write(description))
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=- 45 * DEGREES)

        num_spheres_side = 4  # Reduced from 5
        cube_side = 3
        sphere_radius = cube_side/(num_spheres_side * 3)
        spheres = VGroup()

        # Show axes for reference
        axes = ThreeDAxes(
            x_range=(-2, 2),
            y_range=(-2, 2),
            z_range=(-2, 2)
        )
        
        # Move labels to fixed frame positions to avoid overlapping
        x_label = Text("X", font_size=24).to_corner(DR).shift(UP * 1.5 + LEFT * 3)
        y_label = Text("Y", font_size=24).to_corner(DL).shift(UP * 1.5 + RIGHT * 3)
        z_label = Text("Z", font_size=24).to_corner(UL).shift(DOWN * 1.5 + RIGHT * 3)
        
        self.add(axes)
        self.add_fixed_in_frame_mobjects(x_label, y_label, z_label)
        
        # Create and add spheres with educational explanation
        building_text = Text(
            "Building a 4×4×4 cube of spheres...",
            font_size=24
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(building_text)
        self.play(Write(building_text))

        # Build the cube layer by layer
        layers = []
        for z in range(num_spheres_side):
            layer = VGroup()
            layer_spheres = []
            for x in range(num_spheres_side):
                for y in range(num_spheres_side):
                    sphere = Sphere(
                        radius=sphere_radius, 
                        fill_opacity=0.8, 
                        color=RED,
                        resolution=(8, 8)  # Lower resolution for better performance
                    ).shift(
                        np.array([
                            -cube_side/2 + (cube_side/(num_spheres_side-1))*x,
                            -cube_side/2 + (cube_side/(num_spheres_side-1))*y,
                            -cube_side/2 + (cube_side/(num_spheres_side-1))*z,
                            ])
                    )
                    layer.add(sphere)
                    layer_spheres.append(sphere)
                    spheres.add(sphere)
            
            layers.append(layer)
            
        # Animate adding layers
        layer_text = None
        for i, layer in enumerate(layers):
            if layer_text:
                self.play(FadeOut(layer_text))
                
            layer_text = Text(
                f"Adding layer {i+1} of {num_spheres_side}",
                font_size=24
            ).to_edge(DOWN)
            
            self.add_fixed_in_frame_mobjects(layer_text)
            
            self.play(
                FadeOut(building_text if i == 0 else None),
                Write(layer_text),
                FadeIn(layer),
                run_time=1
            )
        
        self.add(spheres)
        
        # Explain camera movement
        camera_text = Text(
            "Rotating the camera to view the cube from different angles",
            font_size=24
        ).to_edge(DOWN)
        
        if layer_text:
            self.play(FadeOut(layer_text))
            
        self.add_fixed_in_frame_mobjects(camera_text)
        self.play(Write(camera_text))
        
        self.move_camera(
            theta = -135*DEGREES,
            phi = 75*DEGREES,
            run_time = 5,
            about_point = ORIGIN
        )
        
        self.wait(2)
        
        conclusion_text = Text(
            "This simple cube demonstrates basic 3D visualization techniques",
            font_size=24
        ).to_edge(DOWN)
        
        self.play(
            FadeOut(camera_text),
            Write(conclusion_text)
        )
        
        self.wait(2)