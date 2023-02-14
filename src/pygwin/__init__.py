"""
Pygame-Window: Enhanced window management and functionalities for Pygame

Pygame-Window is a Python library that provides an API for managing and
manipulating multiple windows within the Pygame framework, as well as enhancing
their functionalities.

The library uses Pygame's sub-module `pygame._sdl2` to access the low-level
SDL2 library that Pygame is built upon, providing fine-grained control over
window creation and management.
"""

__author__ = "Zenthm"
__version__ = "1.0.0.dev1"

from pygwin.window import Window, WINDOWPOS_CENTERED, WINDOWPOS_UNDEFINED
