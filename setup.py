import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), "r") as f:
    long_description = f.read()

with open(os.path.join(here, "requirements.txt"), "r") as f:
    INSTALL_REQUIRES = f.read().splitlines()

about = {}
with open(os.path.join(here, "betconnect", "__version__.py"), "r") as f:
    exec(f.read(), about)

setup(
    name=about["__title__"],
    version=about["__version__"],
    packages=find_packages(),
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    author=about["__author__"],
    author_email="oliverashleyvarney@gmail.com",
    license=about["__license__"],
    package_dir={"betconnect": "betconnect"},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=INSTALL_REQUIRES,
    test_suite="tests",
)
