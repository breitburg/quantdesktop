from sys import argv
from desktop.config import __version__

if len(argv) != 1:
    from setuptools import setup, find_packages


    setup(
        name='quantify-desktop',
        version=__version__,
        description='Слежка за пользователями с их согласия',
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            'requests',
            'pynput',
            'pystray',
            'pillow',
            'psutil'
          ],
    )