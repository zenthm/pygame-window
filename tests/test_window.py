import pygame

import pygwin


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
    pygame.quit()


def test_methods():
    pygame.init()
    window = pygwin.Window()
    window.destroy()
    window = pygwin.Window()
    window.fill()
    window.update()
    window.hide()
    window.show()
    window.minimize()
    window.maximize()
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
