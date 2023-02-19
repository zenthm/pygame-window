"""
Window Descriptors

This module contains descriptor classes that provide a convenient and
streamlined interface for accessing and manipulating window properties
such as title, size, fullscreen, visibility, etc. in a Pygame application.

These descriptors can be used as attributes of the `Window` class to
manage the behavior and appearance of windows in a Pygame application.
"""


class TitleDescriptor:
    """Descriptor for the window title."""

    def __get__(self, instance, owner):
        return instance.__window__.title

    def __set__(self, instance, value):
        instance.__window__.title = value


class SizeDescriptor:
    """Descriptor for the window size."""

    def __get__(self, instance, owner):
        return instance.__window__.size

    def __set__(self, instance, value):
        instance.__window__.size = value


class PositionDescriptor:
    """Descriptor for the window position."""

    def __get__(self, instance, owner):
        return instance.__window__.position

    def __set__(self, instance, value):
        instance.__window__.position = value


class FullscreenDescriptor:
    """Descriptor for the fullscreen state of the window."""

    def __get__(self, instance, owner):
        return instance.__dict__["fullscreen"]

    def __set__(self, instance, value):
        if value:
            instance.__window__.set_fullscreen(True)
        else:
            instance.__window__.set_windowed()


class VisibleDescriptor:
    """Descriptor for the visibility of the window."""

    def __get__(self, instance, owner):
        return instance.__dict__["visible"]

    def __set__(self, instance, value):
        if value:
            instance.__window__.show()
        else:
            instance.__window__.hide()


class BorderlessDescriptor:
    """Descriptor for the borderless state of the window."""

    def __get__(self, instance, owner):
        return instance.__window__.borderless

    def __set__(self, instance, value):
        instance.__window__.borderless = not value


class ResizableDescriptor:
    """Descriptor for the resizability of the window."""

    def __get__(self, instance, owner):
        return instance.__window__.resizable

    def __set__(self, instance, value):
        instance.__window__.resizable = value


class MinimizedDescriptor:
    """Descriptor for the minimized state of the window."""

    def __get__(self, instance, owner):
        return instance.__dict__["minimized"]

    def __set__(self, instance, value):
        if instance.__dict__["minimized"] != value:
            instance.__window__.minimize()


class MaximizedDescriptor:
    """Descriptor for the maximized state of the window."""

    def __get__(self, instance, owner):
        return instance.__dict__["maximized"]

    def __set__(self, instance, value):
        if instance.__dict__["maximized"] != value:
            instance.__window__.maximize()
