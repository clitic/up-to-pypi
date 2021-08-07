import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

with open("requirements.txt") as f:
    REQUIREMENTS = [req.replace("\n", "") for req in f.readlines()]

setup(
    name = "up_to_pypi",
    version = "2.1.4",
    description = "a gui utility for uploading packages to pypi",
    long_description = README,
    long_description_content_type = "text/markdown",
    keywords = ["pypi", "uploader", "wheel"],
    url = "https://github.com/360modder/up-to-pypi",
    author = "360modder",
    author_email = "apoorv9450@gmail.com",
    license = "MIT",
    python_requires = ">= 3.6",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages = [
        "up_to_pypi",
        "up_to_pypi/components",
    ],
    package_data = {
        "up_to_pypi": ["settings/*.json", "templates/*.txt", "images/*.png"]
    },
    include_package_data = True,
    install_requires = REQUIREMENTS,
    entry_points = {
        "console_scripts": [
            "up-to-pypi = up_to_pypi.launcher:main",
        ]
    },
)
