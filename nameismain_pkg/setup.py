from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # list your package dependencies here
    ],
    entry_points={
        'console_scripts': [
            'mypackage=nameismain_pkg.nameismain:nameismain',
        ],
    },
)
