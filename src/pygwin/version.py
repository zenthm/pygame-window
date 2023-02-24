"""
This module provides the version information for Pygame-Window.

Pygame-Window's version number is stored in a file named "VERSION" in the same
directory as this module. The version number is read from the file and made
available as the module-level variable VERSION.

Example usage:
    >>> from pygwin.version import VERSION
    >>> print(VERSION)
    1.0.0
"""

import os

# Get the path to the VERSION file
VERSION_FILE = os.path.join(os.path.dirname(__file__), "VERSION")

# Read the version number from the VERSION file
with open(VERSION_FILE) as f:
    VERSION = f.read().strip()

# Clean up by removing the reference to the os module
del os
