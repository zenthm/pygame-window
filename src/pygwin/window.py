"""
Custom Window Class for Pygame

This module defines a custom `Window` class for Pygame that streamlines the
creation and management of windows in Pygame applications. The class offers a
variety of customizable features and convenient window management functions
to make the development process smoother and more efficient.
"""

from pygame import _sdl2 as sdl
from pygame._sdl2.video import WINDOWPOS_CENTERED, WINDOWPOS_UNDEFINED

from pygwin import _window_descriptors as windes


class Window:
    """A custom `Window` class for Pygame.

    This class is a custom class for Pygame that streamlines the creation and
    management of windows in Pygame applications. It offers a variety of
    customizable features and convenient window management functions to make
    the development process smoother and more efficient.

    Attributes:
        title (str): The title of the window, which is displayed in the
            window's title bar.
        size (Tuple[int, int]): The width and height of the window, specified
            as a tuple of integers.
        position (Union[Tuple[int, int], int]): The position of the window on
            the screen.
        fullscreen (bool): Whether the window should be displayed in
            fullscreen mode.
        visible (bool): Whether the window is currently visible.
        borderless (bool): Whether the window has a border.
        resizable (bool): Whether the user can resize the window.
        minimized (bool): Whether the window is currently minimized.
        maximized (bool): Whether the window is currently maximized.
        __window__ (sdl.video.Window): An instance of `sdl.video.Window`
            representing the window.
        __renderer__ (sdl.video.Renderer): An instance of `sdl.video.Renderer`
            associated with the window.
    """

    title = windes.TitleDescriptor()
    size = windes.SizeDescriptor()
    position = windes.PositionDescriptor()
    fullscreen = windes.FullscreenDescriptor()
    visible = windes.VisibleDescriptor()
    borderless = windes.BorderlessDescriptor()
    resizable = windes.ResizableDescriptor()
    minimize = windes.MinimizeDescriptor()
    maximize = windes.MaximizeDescriptor()

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

    def __init__(
        self,
        title="pygame",
        size=(640, 480),
        position=WINDOWPOS_CENTERED,
        fullscreen=False,
        visible=False,
        borderless=False,
        resizable=False,
        minimized=False,
        maximized=False,
    ):
        """Initializes a window.

        Args:
            title (str): The title of the window, which is displayed in the
                window's title bar.
                Default is "pygame".
            size (Tuple[int, int]): The width and height of the window,
                specified as a tuple of integers.
                Default is (640, 480).
            position (Union[Tuple[int, int], int]): The position of the window
                on the screen.
                If specified as a tuple, it should contain the x and y
                coordinates of the top-left corner of the window.
                If specified as an integer, it can be one of the `WINDOWPOS_*`
                constants defined in `pygame`.
                Default is `WINDOWPOS_CENTERED`.
            fullscreen (bool): Whether the window should be displayed in
                fullscreen mode.
                Default is False.
            visible (bool): Whether the window should be visible when it is
                first created.
                Default is False.
            borderless (bool): Whether the window should have a border.
                Default is False.
            resizable (bool): Whether the user should be able to resize the
                window.
                Default is False.
            minimized (bool): Whether the window should be minimized when it is
                first created.
                Default is False.
            maximized (bool): Whether the window should be maximized when it is
                first created.
                Default is False.

        Returns:
            None
        """
        self.__window__ = sdl.video.Window(hidden=True)
        self.__renderer__ = sdl.video.Renderer(self.__window__)

        self.title = title
        self.size = size
        self.position = position
        self.fullscreen = fullscreen
        self.visible = visible
        self.borderless = borderless
        self.resizable = resizable
        self.minimized = minimized
        self.maximized = maximized
