"""
This module redefines the dunder variables for specialized use cases.
By default, these variables are set by Python based on the module's location
and package hierarchy. However, in some cases, it may be necessary to modify
these variables for dynamic imports or package restructuring.

Note that redefining these variables can have unintended consequences and
should be done with caution. It may break relative imports and confuse the
Python interpreter when loading modules. If you need to modify these variables,
make sure you fully understand the consequences and test your code thoroughly
to ensure that it works correctly.
"""

__all__ = [
    "__author__",
    "__package__",
    "__version__",
]

# pylint: disable=W0622
__author__ = "Zenthm"
__package__ = "pygame-window"
__version__ = "1.0.0b1"
