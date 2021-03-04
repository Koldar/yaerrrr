import os
from typing import List, Tuple

import setuptools
from yaerrrr import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def get_dependencies() -> List[str]:
    with open("requirements.txt", mode="r") as f:
        requirements = f.readlines()

    return list(map(lambda l: l.split('==')[0], requirements))


setuptools.setup(
    name="yaerrrr",
    version=version.VERSION,
    author="Massimo Bono",
    author_email="massimobono1@gmail.com",
    description="Generate ER diagrams with python and graphviz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # license=license_value,
    url="https://github.com/Koldar/yaerrrr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=get_dependencies(),
    python_requires='>=3.6',
    # add for installation script to work
    # entry_points={"console_scripts": ["pmakeup=pmakeup.main:main"]},
)
