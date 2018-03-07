[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/AndreasJacobsen/noseCV/blob/master/LICENSE) 
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

# Rhino 
A Python application that allows a user to controll the mouse using the nose with help from [OpenCV](https://opencv.org/) and [PyUserInput](https://github.com/PyUserInput/PyUserInput)

## Installation 
Rhino requires [OpenCV 3.4](https://github.com/opencv/opencv/releases/tag/3.4.0) but may work in other version, only running OpenCV as a pip-package may significantly reduce performance. Run "pip install requirements.txt" to install base dependencies, we recomend using a Python virtual environment 
For mouse movement there are differnet requirements for different operating systems
#### Windows requirements
* [pywin32](https://sourceforge.net/projects/pywin32/)
* [pyHook](https://sourceforge.net/projects/pywin32/)

#### Linux requirements
* [xlib](https://github.com/python-xlib/python-xlib)  (comes default with most Linux distros) 

#### MacOS / OSX requirements
* [Quartz](https://www.xquartz.org/)
* [AppKit](https://developer.apple.com/documentation/appkit)


