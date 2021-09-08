import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='pyautomationml',
    description='Library for processing AutomationML files in python',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/CIIRC-ISI/PyAML",
    author="CIIRC ISI Microteam",
    author_email="doudape1@fel.cvut.cz",
    version='1.1.0',
    packages=['pyautomationml'],
    license="BSD",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"],
    install_requires=[
        'lxml',
    ],
)
