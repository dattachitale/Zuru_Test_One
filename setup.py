from setuptools import setup, find_packages


setup(
    name='pyls',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyls = pyls:main_function'
        ]
    }
)