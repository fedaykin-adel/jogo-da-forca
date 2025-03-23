from setuptools import setup, find_packages

setup(
    name="forca",
    version="0.1.0",
    description="Um jogo da forca em Python",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.23.5"
    ],
    entry_points={
        "console_scripts": [
            "forca=main:main",
        ],
    },
    python_requires=">=3.10",
)