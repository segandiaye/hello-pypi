from setuptools import setup, find_packages

setup(
    name='hello-pypi-segandiaye',  
    version='0.1.0',
    packages=find_packages(),
    author='Sega NDIAYE',
    author_email='ndiaye.sega.pro@example.com',
    description='A simple example package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/segandiaye/hello-pypi',  # optional
    python_requires='>=3.10',
)