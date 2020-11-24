import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="up_to_pypi",
    version="1.0.8",
    description="A PyQt5 GUI Uploder For Uploading Packages To PyPi",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=['gui', 'upload', 'pypi', 'twine', 'uploader', 'PyQt5'],
    url="https://github.com/360modder/up-to-pypi",
    author="360modder",
    author_email="apoorv9450@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["up_to_pypi"],
    package_data={'up_to_pypi':['*.pyw', 'assets/*ui','images/*.png', 'assets/*.xml']},
    include_package_data=True,
    install_requires=["PyQt5", "pyqt5_material", "twine", "jinja2"],
    entry_points={
        "console_scripts": [
            "up-to-pypi=up_to_pypi.main:main",
            "uptopypi=up_to_pypi.main:main",
        ]
    },
)
