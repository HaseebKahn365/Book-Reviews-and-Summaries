"""
Graphics Engine Module
Provides core functionality and dynamic plugin loading.
"""
import importlib


def load_plugin(plugin_name):
    """
    Dynamically load a plugin by name from the plugins namespace.
    
    Args:
        plugin_name (str): Name of the plugin module (e.g., "svg")
    
    Returns:
        module: The imported plugin module
    
    Example:
        >>> svg_plugin = load_plugin("svg")
    """
    module_path = f"plugins.{plugin_name}"
    return importlib.import_module(module_path)


def register_format(format_name):
    """
    Utility function that plugins can use to register themselves.
    This demonstrates a shared utility accessible via imports.
    """
    print(f"[Engine] Registered format: {format_name}")
    return True


def render(data, format_type):
    """
    Core rendering function that plugins might utilize.
    """
    print(f"[Engine] Rendering {format_type} data...")
    return f"Rendered: {data}"
