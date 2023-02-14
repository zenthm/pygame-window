"""
Custom Window Class for Pygame

This module defines a custom `Window` class for Pygame that streamlines the
creation and management of windows in Pygame applications. The class offers a
variety of customizable features and convenient window management functions
to make the development process smoother and more efficient.
"""

from pygame._sdl2.video import WINDOWPOS_CENTERED, WINDOWPOS_UNDEFINED


class Window:
    """A custom `Window` class for Pygame.

    This class is a custom class for Pygame that streamlines the creation and
    management of windows in Pygame applications. It offers a variety of
    customizable features and convenient window management functions to make
    the development process smoother and more efficient.
    """

    __dict__ = dict(
        title="pygame",
        size=(640, 480),
        position=WINDOWPOS_CENTERED,
        fullscreen=False,
        visible=False,
        borderless=False,
        resizable=False,
        minimized=False,
        maximized=False,
    )
