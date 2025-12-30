"""
SVG Plugin Module
Demonstrates imports to access engine utilities in namespace packages.
"""

# For namespace packages, we can use absolute imports
# since both directories are in sys.path and merge into 'graphics'
from graphics.engine import register_format, render

# Note: Relative imports (from ...engine import ...) work in regular packages
# but can be tricky with namespace packages. The absolute import above
# demonstrates how plugins access the core engine across namespace boundaries.


class SVGDecoder:
    """SVG format decoder implementation."""
    
    def __init__(self):
        # Register this format with the engine
        register_format("SVG")
        self.format_name = "SVG"
    
    def decode(self, svg_data):
        """
        Decode SVG data.
        
        Args:
            svg_data (str): SVG content as string
        
        Returns:
            str: Decoded/rendered output
        """
        print(f"[SVG Plugin] Decoding SVG data...")
        # Use the engine's render function
        return render(svg_data, self.format_name)
    
    def info(self):
        """Return plugin information."""
        return {
            "name": "SVG Decoder",
            "version": "1.0",
            "formats": ["svg", "svgz"]
        }


# Module-level convenience function
def decode_svg(svg_content):
    """
    Convenience function to decode SVG without instantiating the class.
    """
    decoder = SVGDecoder()
    return decoder.decode(svg_content)
