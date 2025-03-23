# Manimations

This repository showcases my journey learning Manim, the mathematical animation engine created by 3Blue1Brown. I'm using this project to explore animation techniques, mathematical visualizations, and to improve my Python skills.

## Learning Journey

As I explore Manim's capabilities, I'll be adding various animations that demonstrate different concepts and techniques. This repository serves as both a learning record and a showcase of my progress.

## Projects

### Basic Morphing
A series of animations showing spheres morphing into different 3D shapes.

https://github.com/RanL703/manimations/raw/main/media/videos/basic_morphing/1080p60/BasicMorphing.mp4

Features:
- Spheres → Tetrahedron (Red)
- Spheres → Octahedron (Orange)
- Spheres → Dodecahedron (Yellow)
- Spheres → Icosahedron (Green)
- Spheres → Sphere (Teal)
- Spheres → Torus (Purple)

### Basic Shapes
Minimal version with just one shape transformation (tetrahedron).

### Spheres in Shapes
Exploring more complex transformations and animations.

## Getting Started

### Installation

```bash
pip install manim
```

### Running the Animations

```bash
# Low quality (fastest)
manim -pql basic_shapes.py BasicShapes
manim -pql basic_morphing.py BasicMorphing

# Medium quality
manim -pqm basic_morphing.py BasicMorphing

# High quality (slowest)
manim -pqh basic_morphing.py BasicMorphing
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