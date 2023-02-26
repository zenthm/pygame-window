import pygame
import pytest

import pygwin


def test_arguments():
    pygame.init()
    window = pygwin.Window(
        title="test",
        size=(800, 600),
        position=(0, 0),
        fullscreen=True,
        visible=True,
        borderless=True,
        resizable=True,
        minimized=True,
        maximized=True,
    )
    window.destroy()

    with pytest.raises(AttributeError):
        window = pygwin.Window(test=None)
        window.destroy()

    pygame.quit()


def test_attributes():
    pygame.init()
    window = pygwin.Window()
    window.fullscreen = True
    window.fullscreen = False
    window.visible = True
    window.visible = False
    window.borderless = True
    window.borderless = False
    window.resizable = True
    window.resizable = False
    window.minimized = True
    window.minimized = False
    window.maximized = True
    window.maximized = False

    window.title
    window.size
    window.position
    window.fullscreen
    window.visible
    window.borderless
    window.resizable
    window.minimized
    window.maximized

    with pytest.raises(AttributeError):
        window.test

    window.destroy()
    pygame.quit()


def test_methods():
    pygame.init()
    window = pygwin.Window()
    window.fill()
    window.update()
    window.hide()
    window.show()
    window.minimize()
    window.maximize()
    window.restore()
    window.destroy()
    pygame.quit()


def test_magic_methods():
    pygame.init()
    window = pygwin.Window()
    window == window
    window == "window"
    window != window
    window != "window"

    print(window)
    pygame.quit()
