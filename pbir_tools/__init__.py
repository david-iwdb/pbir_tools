"""
pbir_tools - A Python library to create and edit PBIX files stored in the PBIR format.

This package provides utilities for working with Power BI files using the PBIR format.
"""

__version__ = "0.1.0"
__author__ = "David IWDB"
__license__ = "MIT"

# Import main classes and functions for easy access
from .pbir_handler import PBIRHandler

__all__ = ["PBIRHandler", "__version__"]
