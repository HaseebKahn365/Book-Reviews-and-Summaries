#!/usr/bin/env python3
"""
Demo script for the plugin-driven graphics framework.
Demonstrates namespace packages, dynamic loading, and relative imports.
"""

import sys
from pathlib import Path

# Add current directory to sys.path to find graphics module
base_dir = Path(__file__).parent
sys.path.insert(0, str(base_dir))

# Now we can import from graphics
from graphics.engine import load_plugin

def main():
    print("=" * 60)
    print("Plugin-Driven Graphics Framework Demo")
    print("=" * 60)
    
    # Demonstrate dynamic plugin loading
    print("\n1. Loading SVG plugin dynamically...")
    svg_module = load_plugin("svg")
    print(f"   Loaded module: {svg_module}")
    
    # Use the plugin
    print("\n2. Creating SVG decoder instance...")
    decoder = svg_module.SVGDecoder()
    
    # Get plugin info
    print("\n3. Plugin information:")
    info = decoder.info()
    for key, value in info.items():
        print(f"   {key}: {value}")
    
    # Decode some SVG data
    print("\n4. Decoding SVG data...")
    sample_svg = '<svg><circle cx="50" cy="50" r="40"/></svg>'
    result = decoder.decode(sample_svg)
    print(f"   Result: {result}")
    
    # Use convenience function
    print("\n5. Using module-level convenience function...")
    result2 = svg_module.decode_svg('<svg><rect width="100" height="100"/></svg>')
    print(f"   Result: {result2}")
    
    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)
    
    # Show the namespace package structure
    print("\n6. Namespace package structure:")
    print(f"   graphics.__path__ = {__import__('graphics').__path__}")


if __name__ == "__main__":
    main()
