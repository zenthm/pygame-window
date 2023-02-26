"""
This module defines a custom `Window` class for Pygame that streamlines the
creation and management of windows in Pygame applications. The class offers a
variety of customizable features and convenient window management functions
to make the development process smoother and more efficient.
"""

import pygame
from pygame import _sdl2 as sdl

# Define window constants
WINDOWPOS_CENTERED = 805240832
WINDOWPOS_UNDEFINED = 536805376


class Window:
    """
    A custom `Window` class for Pygame.

    This class is a custom class for Pygame that streamlines the creation and
    management of windows in Pygame applications. It offers a variety of
    customizable features and convenient window management functions to make
    the development process smoother and more efficient.

    :ivar str title: The title of the window.
    :ivar Tuple[int, int] size: The width and height of the window.
    :ivar Union[int, Tuple[int, int]] position: The position of the window on
        the screen.
    :ivar bool fullscreen: Whether the window is displayed in fullscreen mode.
    :ivar bool visible: Whether the window is visible.
    :ivar bool borderless: Whether the window has a border.
    :ivar bool resizable: Whether the window can be resized by the user.
    :ivar bool minimized: Whether the window is currently minimized.
    :ivar bool maximized: Whether the window is currently maximized.
    """

    # Window configurations
    __dict__ = {
        "title": "pygame",
        "size": (640, 480),
        "position": WINDOWPOS_CENTERED,
        "fullscreen": False,
        "visible": False,
        "borderless": False,
        "resizable": False,
        "minimized": False,
        "maximized": False,
    }

    def __init__(self, **args):
        """
        Initializes a new window object.

        :param str title: The title of the window. Default is "pygame".
        :param Tuple[int, int] size: The width and height of the window.
            Default is (640, 480).
        :param Union[int, Tuple[int, int]] position: The position of the window
            on the screen. Default is `WINDOWPOS_CENTERED`.
        :param bool fullscreen: Whether the window should be displayed in
            fullscreen mode. Default is False.
        :param bool visible: Whether the window should be visible when it is
            first created. Default is False.
        :param bool borderless: Whether the window should have a border.
            Default is False.
        :param bool resizable: Whether the user should be able to resize the
            window. Default is False.
        :param bool minimized: Whether the window should be minimized when it
            is first created. Default is False.
        :param bool maximized: Whether the window should be maximized when it
            is first created. Default is False.

        :raises ValueError: If any parameter has an invalid value.
        :raises AttributeError: If an invalid parameter is specified.
        """
        self.__window__ = sdl.Window(hidden=True)
        self.__renderer__ = sdl.Renderer(self.__window__)

        for key, value in self.__dict__.items():
            setattr(self, key, value)

        for key, value in args.items():
            if key in self.__dict__:
                setattr(self, key, value)
            else:
                raise AttributeError(f"'Window' type has no attribute '{key}'")

    def __getattr__(self, name):
        """
        Called when an attribute lookup has not found the attribute in the usual
        places (i.e., it is not an instance attribute nor is it found in the
        class tree for `self`). This method looks for the attribute in the
        `__dict__` dictionary and returns it if found.

        :param str name: The name of the attribute to retrieve.
        :return: The value of the attribute if found.
        :raises AttributeError: If the attribute is not found in the `__dict__`
            dictionary.
        """
        if name in self.__dict__:
            return self.__dict__[name]
        return self.__getattribute__(name)

    def __setattr__(self, name, value):
        """
        Called when an attribute is set on an instance of the class.

        This method first checks if the attribute already exists in the
        instance's `__dict__` dictionary. If it does, the method updates the
        existing attribute value in the dictionary. Otherwise, the method calls
        the `super()` function to invoke the base class's `__setattr__` method,
        which sets the attribute on the instance using the default behavior.

        :param str name: The name of the attribute to set.
        :param Any value: The value to set the attribute to.
        """
        if name in self.__dict__:
            self.__dict__[name] = value
        super().__setattr__(name, value)

    def __eq__(self, other):
        """
        Compare this instance to another object for equality.

        This method compares the instance's `__window__` attribute to the
        `other` object. It returns `True` if they are equal and `False`
        otherwise. Note that this implementation assumes that the `other`
        object is of the same type as the instance.

        :param other: The object to compare to this instance.
        :return: `True` if this instance and `other` are equal, `False`
            otherwise.
        """
        return self.__window__ == other

    def __ne__(self, other):
        """
        Compare this instance to another object for inequality.

        This method compares the instance's `__window__` attribute to the
        `other` object. It returns `True` if they are not equal and `False`
        otherwise. Note that this implementation assumes that the `other`
        object is of the same type as the instance.

        :param other: The object to compare to this instance.
        :return: `True` if this instance and `other` are not equal, `False`
            otherwise.
        """
        return self.__window__ != other

    def __repr__(self):
        """
        Return a string representation of this instance that can be used to
        recreate the object.

        This method returns a formatted string that includes the `title` and
        `size` attributes of the instance. The returned string has the format
        `<Window(title size)>`, where `title` and `size` are the values of the
        corresponding attributes of the instance.

        :return: A string representation of this instance.
        """
        return f"<Window({self.title} {self.size})>"

    def fill(self, color=(0, 0, 0)):
        """
        Fill the window with a specified color.

        This method sets the `draw_color` attribute of the `__renderer__`
        attribute of the instance to the specified `color`, which can be either
        a tuple of RGB values or a `ColorValue` object from the `pygame`
        module. If `color` is not specified, the default color is set to
        (0, 0, 0). Then, this method calls the `clear` method of the
        `__renderer__` attribute to replace the contents of the window with the
        specified color.

        :param Union[Tuple[int, int, int], ColorValue] color: The RGB values
            (0-255) of the color to fill the window with, specified as a tuple
            of integers, or a `ColorValue` object from `pygame`. If not
            specified, the default color is (0, 0, 0).
        """
        self.__renderer__.draw_color = pygame.Color(color)
        self.__renderer__.clear()

    def update(self):
        """
        Refresh the window to display any changes made.

        This method calls the `present` method of the `__renderer__` attribute
        of the instance, which updates the window to reflect any changes made
        to its contents, such as drawing new shapes or changing the color of
        existing ones.
        """
        self.__renderer__.present()

    def hide(self):
        """
        Hide the window.

        This method sets the `visible` attribute of the instance to `False`,
        effectively making the window invisible to the user.
        """
        self.visible = False

    def show(self):
        """
        Make the window visible.

        This method sets the `visible` attribute of the instance to `True`,
        making the window visible to the user.
        """
        self.visible = True

    def minimize(self):
        """
        Minimize the window.

        This method reduces the size of the window to its taskbar
        representation.
        """
        self.__window__.minimize()

    def maximize(self):
        """
        Maximize the window.

        This method expands the window to fill the entire screen.
        """
        self.__window__.maximize()

    def restore(self):
        """
        Restore the window.

        This method restores the window to its previous size and position after
        it has been minimized or maximized.
        """
        self.__window__.restore()

    def destroy(self):
        """
        Close the window and release any system resources associated with it.

        This method calls the `destroy` method of the `__window__` attribute of
        the instance, which presumably is an instance of a GUI toolkit's window
        class. This method frees up any system resources used by the window.
        """
        self.__window__.destroy()

    # Getters
    @property
    def title(self):
        """
        Get the title of the window.

        :return: The title of the window as a string.
        """
        return self.__window__.__dict__["title"]

    @property
    def size(self):
        """
        Get the size of the window.

        :return: The size of the window as a tuple of two integers representing
            the width and height of the window in pixels.
        """
        return self.__window__.__dict__["size"]

    @property
    def position(self):
        """
        Get the position of the window.

        :return: The position of the window as a tuple of two integers representing
            the x and y coordinates of the top-left corner of the window in pixels.
        """
        return self.__window__.__dict__["position"]

    @property
    def fullscreen(self):
        """
        Get whether the window is currently displayed in fullscreen mode.

        :return: True if the window is currently displayed in fullscreen mode, False
            otherwise.
        """
        return self.__window__.__dict__["fullscreen"]

    @property
    def visible(self):
        """
        Get whether the window is currently visible to the user.

        :return: True if the window is currently visible, False otherwise.
        """
        return self.__window__.__dict__["visible"]

    @property
    def borderless(self):
        """
        Get whether the window is currently borderless.

        :return: True if the window is currently borderless, False otherwise.
        """
        return self.__window__.__dict__["borderless"]

    @property
    def resizable(self):
        """
        Get whether the window is currently resizable by the user.

        :return: True if the window is currently resizable, False otherwise.
        """
        return self.__window__.__dict__["resizable"]

    @property
    def minimized(self):
        """
        Get whether the window is currently minimized.

        :return: True if the window is currently minimized, False otherwise.
        """
        return self.__window__.__dict__["minimized"]

    @property
    def maximized(self):
        """
        Get whether the window is currently maximized.

        :return: True if the window is currently maximized, False otherwise.
        """
        return self.__window__.__dict__["maximized"]

    # Setters
    @title.setter
    def title(self, value):
        """
        Set the title of the window.

        :param str new_title: The new title to set.
        """
        self.__window__.title = value

    @size.setter
    def size(self, value):
        """
        Set the size of the window.

        :param Tuple[int, int] new_size: The new size to set, specified as a
            tuple of two integers representing the width and height of the
            window in pixels.
        """
        self.__window__.size = value

    @position.setter
    def position(self, value):
        """
        Set the position of the window.

        :param Tuple[int, int] new_position: The new position to set, specified as
            a tuple of two integers representing the x and y coordinates of the
            top-left corner of the window in pixels.
        """
        self.__window__.position = value

    @fullscreen.setter
    def fullscreen(self, value):
        """
        Set whether the window should be displayed in fullscreen mode.

        :param bool value: True if the window should be displayed in fullscreen
            mode, False otherwise.
        """
        if value:
            self.__window__.set_fullscreen(True)
        else:
            self.__window__.set_windowed()

    @visible.setter
    def visible(self, value):
        """
        Set whether the window should be visible to the user.

        :param bool value: True if the window should be visible, False otherwise.
        """
        if value:
            self.__window__.show()
        else:
            self.__window__.hide()

    @borderless.setter
    def borderless(self, value):
        """
        Set whether the window should have borders.

        :param bool value: True if the window should be borderless, False
            otherwise.
        """
        self.__window__.borderless = not value

    @resizable.setter
    def resizable(self, value):
        """
        Set whether the window can be resized by the user.

        :param bool value: True if the window should be resizable, False
            otherwise.
        """
        self.__window__.resizable = value

    @minimized.setter
    def minimized(self, value):
        """
        Set whether the window should be maximized.

        :param bool value: True if the window should be maximized, False
            otherwise.
        """
        if value:
            self.__window__.minimize()
        else:
            self.__window__.restore()

    @maximized.setter
    def maximized(self, value):
        """
        Set whether the window should be minimized.

        :param bool value: True if the window should be minimized, False
            otherwise.
        """
        if value:
            self.__window__.maximize()
        else:
            self.__window__.restore()
