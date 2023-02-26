"""
Pygame-Window is a Python library that provides an API for managing and
manipulating multiple windows within the Pygame framework, as well as enhancing
their functionalities.

The library uses Pygame's sub-module `pygame._sdl2` to access the low-level
SDL2 library that Pygame is built upon, providing fine-grained control over
window creation and management.
"""

# Import attributes
from pygwin.__attr__ import *  # isort: skip

# Import window tools
from pygwin import window
from pygwin.window import WINDOWPOS_CENTERED, WINDOWPOS_UNDEFINED, Window
