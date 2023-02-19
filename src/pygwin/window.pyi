from typing import Tuple, Union
from pygame import Color

WINDOWPOS_CENTERED: int
WINDOWPOS_UNDEFINED: int

class Window:
    title: str
    size: Tuple[int, int]
    position: Union[int, Tuple[int, int]]
    fullscreen: bool
    visible: bool
    borderless: bool
    resizable: bool
    minimized: bool
    maximized: bool

    def __init__(
        self,
        title: str = "pygame",
        size: Tuple[int, int] = (640, 480),
        position: Union[int, Tuple[int, int]] = WINDOWPOS_CENTERED,
        fullscreen: bool = False,
        visible: bool = False,
        borderless: bool = False,
        resizable: bool = False,
        minimized: bool = False,
        maximized: bool = False,
    ) -> None: ...
    def fill(self, color: Union[Color, Tuple[int, int, int]] = (0, 0, 0)) -> None: ...
    def update(self) -> None: ...
    def hide(self) -> None: ...
    def show(self) -> None: ...
    def minimize(self) -> None: ...
    def maximize(self) -> None: ...
    def destroy(self) -> None: ...
