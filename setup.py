from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='work_tools',  # 包名
    version='1.0.0',  # 版本号
    description='A small example package',
    long_description=long_description,
    author='zack liu',
    author_email='1056559106@qq.com',
    install_requires=[

    ],
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
)
