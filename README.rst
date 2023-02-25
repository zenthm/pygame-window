Pygame-Window
=============

|PyPI version| |Test status| |Coverage Status| |License| |Python Version| |Code style: black| |Imports: isort|

Pygame-Window is a Python library that provides an API for managing and
manipulating multiple windows within the Pygame framework, as well as
enhancing their functionalities.

The library uses Pygame's sub-module ``pygame._sdl2`` to access the
low-level SDL2 library that Pygame is built upon, providing fine-grained
control over window creation and management.

Installation
------------

Pygame-Window can be installed using pip with the following command:

.. code:: bash

   python -m pip install pygame-window

If you want to install Pygame-Window from source, you can clone the
repository from GitHub using the following command:

.. code:: bash

   git clone https://github.com/zenthm/pygame-window.git

Once you have downloaded the source code, you can install Pygame-Window
by running the following command from the root directory of the
repository:

.. code:: bash

   python -m pip install .

License
-------

Pygame-Window is distributed under the MIT License. See the
`license <https://github.com/zenthm/pygame-window/blob/master/LICENSE.rst>`__
file for more information.

Acknowledgments
---------------

I would like to thank the following for their contributions to
Pygame-Window:

-  The Pygame team for creating and maintaining the Pygame library.
-  The SDL development team for creating and maintaining the SDL2
   library.
-  The contributors to Pygame-Window.

Thank you all for your valuable contributions!

Code of Conduct
---------------

I am committed to treating everyone with respect and kindness,
regardless of their background, beliefs, or identity. As a member of the
open source community, I believe it is important to create a welcoming
and inclusive environment for all.

To that end, I ask that anyone who interacts with this project or
contributes to it follow this `Code of
Conduct <https://github.com/zenthm/pygame-window/blob/master/CODE_OF_CONDUCT.rst>`__.
The Code of Conduct outlines specific behaviors that are expected of
contributors and community members, as well as the consequences for
violating the Code of Conduct.

If I observe or experience any behavior that violates this Code of
Conduct, I may take any action I deem appropriate, including warning the
offender or blocking them from further interaction with this project.

I take this Code of Conduct seriously and am committed to creating a
positive and respectful environment for everyone who interacts with this
project.

.. |PyPI version| image:: https://img.shields.io/pypi/v/pygame-window
   :target: https://pypi.org/project/pygame-window/
.. |Test status| image:: https://github.com/zenthm/pygame-window/actions/workflows/test.yml/badge.svg?branch=master
   :target: https://github.com/zenthm/pygame-window/actions/workflows/test.yml
.. |Coverage Status| image:: https://coveralls.io/repos/github/zenthm/pygame-window/badge.svg?branch=master
   :target: https://coveralls.io/github/zenthm/pygame-window?branch=master
.. |License| image:: https://img.shields.io/pypi/l/pygame-window
   :target: https://github.com/zenthm/pygame-window/blob/master/LICENSE.rst
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/pygame-window
   :target: https://www.python.org/downloads/
.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |Imports: isort| image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
   :target: https://pycqa.github.io/isort/
