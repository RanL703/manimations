# Manimations

This repository showcases my journey learning Manim, the mathematical animation engine created by 3Blue1Brown. I'm using this project to explore animation techniques, mathematical visualizations, and to improve my Python skills.

## Learning Journey

As I explore Manim's capabilities, I'll be adding various animations that demonstrate different concepts and techniques. This repository serves as both a learning record and a showcase of my progress.

## Projects

### Basic Morphing
A series of animations showing spheres morphing into different 3D shapes.

![BasicMorphing](./media/videos/basic_morphing/480p15/BasicMorphing.mp4)

Features:
- Spheres → Tetrahedron (Red)
- Spheres → Octahedron (Orange)
- Spheres → Dodecahedron (Yellow)
- Spheres → Icosahedron (Green)
- Spheres → Sphere (Teal)
- Spheres → Torus (Purple)

### Basic Shapes
Minimal version with just one shape transformation (tetrahedron).

### Donut to Sphere morph
An animation showing a generation of a donut shape which then morphs into a sphere.

### Complex Number visualization
This script uses Manim to create sophisticated 3D visualizations of complex functions and their integration in complex analysis. The animations demonstrate fundamental concepts in complex analysis by providing intuitive visual representations of abstract mathematical concepts.

#### Features:

#### Complex Function Visualization
- Renders complex functions as 3D surfaces where:
  - The real and imaginary parts (x,y) form the complex plane
  - The height (z-axis) represents the magnitude |f(z)|
  - Color represents the phase/argument arg(f(z))
- Includes visualizations of common functions:
  - f(z) = z² (quadratic function)
  - f(z) = z³ (cubic function)
  - f(z) = 1/z (function with singularity)

#### Complex Integration Visualization
- Demonstrates integration along different paths:
  - Circular paths
  - Rectangular paths
  - Custom multi-segment paths
- Provides step-by-step animation of the integration process
- Shows the numerical accumulation of the integral
- Illustrates Cauchy's Integral Theorem by showing that:
  - Integrals around closed paths in regions with no singularities ≈ 0
  - Integrals around singularities yield non-zero values

#### Educational Elements
- Clear labels and explanatory text
- Color coding for phase interpretation
- Camera movements to view functions from multiple angles
- Discretization visualization for numerical integration
- Real-time accumulation of integral values along paths

#### Mathematical Concepts Demonstrated
- Complex function mapping from ℂ to ℂ visualized in 3D
- Path integration in the complex plane
- Cauchy's Integral Theorem
- Behavior of functions near singularities
- Numerical integration techniques (trapezoidal rule)

#### Additional Visualizations
The repository also includes a simple `CubeOfSpheres` class demonstrating 3D arrangement capabilities in Manim, which creates a cubic lattice of colored spheres with animated assembly.


## Getting Started

### Installation

```bash
pip install manim
```

### Generating the Animations from Script

```bash
# Low quality (fastest)
manim -pql basic_shapes.py BasicShapes
manim -pql basic_morphing.py BasicMorphing
manim -pql donut2sphere.py DonutToSphere
manim -pql spheresinshapes.py ComplexFunctionVisualization

# Medium quality
manim -pqm basic_morphing.py BasicMorphing
manim -pqm donut2sphere.py DonutToSphere
manim -pqm spheresinshapes.py ComplexFunctionVisualization

# High quality (slowest)
manim -pqh basic_morphing.py BasicMorphing
manim -pqh donut2sphere.py DonutToSphere
manim -pqh spheresinshapes.py ComplexFunctionVisualization
```

## Quality Options

- `-ql` - Low quality (480p, 15fps)
- `-qm` - Medium quality (720p, 30fps)
- `-qh` - High quality (1080p, 60fps)
- `-qk` - 4K quality (2160p, 60fps) - may be very slow

## Notes

- Rendered videos are saved to the `media/videos/` directory
- This repository is continuously evolving as I learn more about Manim
- Feel free to use these examples for your own learning process 
