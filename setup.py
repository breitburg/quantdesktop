from setuptools import setup, find_packages
from sys import argv

if argv[len(argv) - 1] != 'install':
    print('ahhsa')

setup(
    name='quantify-desktop',
    version='1.0.7',
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

