from setuptools import setup, find_packages

# Setup is not required for spark_script.py, but tox wants it
setup(
    name='pyspark-template',
    version='1.0',
    packages=find_packages()
)
