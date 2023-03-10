"""
Setup file for the Pygame-Window package.

This file defines the package metadata and options, including the package name,
version, author information, description, long description, dependencies,
Python version requirements, and other relevant information. It also reads the
`__attr__.py` file for setting up package attributes.

The setup() function is called with the defined metadata options, which are
used by pip to install the package from the PyPI repository.
"""

from pathlib import Path

from setuptools import find_packages, setup

# Setup package attributes
attr_file = Path("src/pygwin/__attr__.py")
attr_info = {"__file__": attr_file}

# Read package attributes
with open(attr_file, "r", encoding="UTF-8") as f:
    content = f.read()
    exec(content, attr_info)

# Read long description from file
with open("README.rst", "r", encoding="UTF-8") as f:
    long_description = f.read()


# Read requirements from files
def read_requirements(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        return [line.strip() for line in f.readlines()]


reqs_prod = read_requirements("requirements/prod.txt")
reqs_devs = read_requirements("requirements/devs.txt")
reqs_docs = read_requirements("requirements/docs.txt")
reqs_all = reqs_devs + reqs_docs

# Define package metadata and options
metadata = {
    "name": attr_info["__package__"],
    "version": attr_info["__version__"],
    "author": attr_info["__author__"],
    "author_email": "zenthm.dev@gmail.com",
    "description": "Enhanced window management and functionalities for Pygame",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://pygame-window.readthedocs.io/en/latest/",
    "download_url": "https://pypi.org/project/pygame-window/",
    "project_urls": {
        "Bug Tracker": "https://github.com/zenthm/pygame-window/issues",
        "Documentation": "https://pygame-window.readthedocs.io/en/latest/",
        "Source Code": "https://github.com/zenthm/pygame-window",
    },
    "classifiers": [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: pygame",
        "Typing :: Typed",
    ],
    "license": "MIT",
    "packages": find_packages(where="src"),
    "package_dir": {"": "src"},
    "include_package_data": True,
    "install_requires": reqs_prod,
    "extras_require": {
        "all": reqs_all,
        "devs": reqs_devs,
        "docs": reqs_docs,
    },
    "python_requires": ">=3.7,<3.11",
    "keywords": [
        "python",
        "pygame",
        "window",
        "pygame-library",
        "window-management",
        "multiple-windows",
        "pygame-window",
        "pygame-sdl2",
    ],
    "zip_safe": False,
}

# Call setup with metadata options
setup(**metadata)
