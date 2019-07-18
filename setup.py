from setuptools import setup

setup(
    name='quantify-desktop',
    version='1.0',
    description='Слежка за пользователями с их согласия',
    long_description=open('readme.md').read(),
    packages=['desktop'],
    install_requires=[
        'requests',
        'pynput',
        'pystray'
      ],
)
