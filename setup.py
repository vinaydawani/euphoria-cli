import os
from setuptools import find_packages, setup


def read(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()


setup(
    name="Euphoria_CLI",
    version="0.1.0",
    author="Vinay Dawani",
    author_email="vdawani6@gmail.com",
    description="A small CLI tool to fetch Euphoria's price and stats",
    license="GNU GPL v3",
    url="https://github.com/vinaydawani/euphoria-cli",
    keywords="euphoria WAGMI sWAGMI blockchain rebase token bonding staking bond stake",
    long_description=read("README.md"),
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click", "pyfiglet", "requests", "web3", "halo"],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["euphoria = src.app:euphoria"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
