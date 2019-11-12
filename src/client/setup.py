from setuptools import setup

setup(
    name = 'client',
    version = '0.1.0',
    packages = ['clock'],
    entry_points = {
        'console_scripts': [
            'client = clock.__main__:main'
        ]
    })