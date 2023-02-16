from setuptools import setup, find_packages

with open("README.md", "r", encoding="UTF-8") as f:
    long_description = f.read()

with open("requirements/production.txt", "r", encoding="UTF-8") as f:
    requirements_production = f.read().splitlines()

with open("requirements/development.txt", "r", encoding="UTF-8") as f:
    requirements_development = f.read().splitlines()

with open("requirements/documentation.txt", "r", encoding="UTF-8") as f:
    requirements_documentation = f.read().splitlines()

all_requirements = requirements_development + requirements_documentation

metadata = {
    "name": "pygame-window",
    "version": "1.0.0.dev1",
    "author": "Zenthm",
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
    ],
    "license": "MIT",
    "packages": find_packages(where="src"),
    "package_dir": {"": "src"},
    "include_package_data": True,
    "install_requires": requirements_production,
    "extras_require": {
        "all": all_requirements,
        "development": requirements_development,
        "documentation": requirements_documentation,
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

setup(**metadata)
