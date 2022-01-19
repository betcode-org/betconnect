import os
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(os.path.join(os.path.dirname(__file__), "requirements.txt")) as f:
    INSTALL_REQUIRES = f.read().splitlines()

setup(
    name="betconnect",
    version="0.0.7",
    packages=find_packages(),
    description="A betconnect API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/varneyo/betconnect",
    author="oliver Varney",
    author_email="oliverashleyvarney@gmail.com",
    license="MIT",
    package_dir={"betconnect": "betconnect"},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=INSTALL_REQUIRES,
    test_suite="tests",
)
