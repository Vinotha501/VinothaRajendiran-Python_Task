# setup.py
from setuptools import setup, find_packages

setup(
    name='data_analysis_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'scipy',
        'pytest'
    ],
    author='Your Name',
    author_email='your@email.com',
    description='Data analysis package'
)

