"""
Setup configuration for pbir_tools package.

This file provides backward compatibility with older Python packaging tools.
Modern installations should use pyproject.toml.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="pbir_tools",
    version="0.1.0",
    author="David IWDB",
    description="A Python library to create and edit PBIX files stored in the PBIR format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/david-iwdb/pbir_tools",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/david-iwdb/pbir_tools/issues",
        "Source": "https://github.com/david-iwdb/pbir_tools",
    },
)
