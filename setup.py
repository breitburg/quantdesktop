from sys import argv
__version__ = '1.0.11'

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
            'pillow'
          ],
    )