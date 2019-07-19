from setuptools import setup, find_packages

setup(
    name='quantify-desktop',
    version='1.0.10',
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