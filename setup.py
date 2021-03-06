from setuptools import setup, find_packages

setup(
    name='ordernet-api',
    version='0.0.1',
    packages=find_packages(include='ordernet-api*'),
    description='Client to perform queries from spark system',
    install_requires=[
        'colorama',
        'requests',
        'appdirs==1.4.4',
        'distlib==0.3.0',
        'filelock==3.0.12',
        'six==1.14.0'
    ],
    license='GNU LESSER GENERAL PUBLIC LICENSE',
    python_requires='>=3.6'
)
