from setuptools import find_packages, setup

setup(
    name="monkey-log",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Jerry Mao",
    author_email="jerrym@mit.edu",
    description="A Monkey tool used to interface with and log to the Monkey Client"
)
