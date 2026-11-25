# W8_6

# Menu-Driven SVG Drawing Program

This program allows users to interactively draw shapes and save them as SVG files. It uses the `svgwrite` library to create and manipulate SVG drawings.

## Features
- Draw a square (rectangle with equal sides)
- Draw a circle
- Save the SVG file with pretty formatting
- Exit the program

## Instructions
1. The program starts by initializing a `Drawing` object.
2. Users can choose to draw a square or a circle.
3. When saving, the program confirms the filename and asks for user confirmation before writing.
4. The SVG file is saved with 2-space indentation for readability.

## Notes
- The `Drawing` object is passed by reference, so changes made in functions affect the original object.
- Ensure `svgwrite` is installed using `pip install svgwrite` before running the program.