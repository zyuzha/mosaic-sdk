from setuptools import setup, find_packages

setup(
    name='mosaic-sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests', 'numpy'],
    description='SDK for exploring the Infinite Backrooms.',
    author='zyuzha',
    license='MIT',
)