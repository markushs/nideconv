import os
from setuptools import setup, find_packages

# HARDCODED VERSION FROM PREVIOUS (NOW DEPREACATED) version.py
VERSION = "0.1.0rc6"

# Read requirements.txt and use it for the 'install_requires' parameter
def read_requirements():
    with open('requirements.txt', 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

# Find all packages in the current directory
PACKAGES = find_packages()

# Define options for setup
opts = dict(name="nideconv",
            version=VERSION,
            packages=PACKAGES,
            install_requires=read_requirements())

# Run setup
if __name__ == '__main__':
    setup(**opts)
