from typing import Tuple, Type

from pygwin.window import Window

class TitleDescriptor:
    def __get__(self, instance: Window, owner: Type[Window]) -> str: ...
    def __set__(self, instance: Window, value: str) -> None: ...

class SizeDescriptor:
    def __get__(self, instance: Window, owner: Type[Window]) -> Tuple[int, int]: ...
    def __set__(self, instance: Window, value: Tuple[int, int]) -> None: ...

class PositionDescriptor:
    def __get__(self, instance: Window, owner: Type[Window]) -> Tuple[int, int]: ...
    def __set__(self, instance: Window, value: Tuple[int, int]) -> None: ...

class FullscreenDescriptor:
    def __get__(self, instance: Window, owner: Type[Window]) -> bool: ...
    def __set__(self, instance: Window, value: bool) -> None: ...

class VisibleDescriptor:
    def __get__(self, instance: Window, owner: Type[Window]) -> bool: ...
    def __set__(self, instance: Window, value: bool) -> None: ...

class BorderlessDescriptor:
    def __get__(self, instance: Window, owner: Type[Window]) -> bool: ...
    def __set__(self, instance: Window, value: bool) -> None: ...

class ResizableDescriptor:
    def __get__(self, instance: Window, owner: Type[Window]) -> bool: ...
    def __set__(self, instance: Window, value: bool) -> None: ...

class MinimizedDescriptor:
    def __get__(self, instance: Window, owner: Type[Window]) -> bool: ...
    def __set__(self, instance: Window, value: bool) -> None: ...

class MaximizedDescriptor:
    def __get__(self, instance: Window, owner: Type[Window]) -> bool: ...
    def __set__(self, instance: Window, value: bool) -> None: ...
