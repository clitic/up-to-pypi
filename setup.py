import pathlib
import platform
from setuptools import setup

plat = platform.system()

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

if __name__ == '__main__':
    if plat.lower().startswith("win") == True:
        setup(
            name="up_to_pypi",
            version="2.0.3.dev",
            description="A PyQt5 GUI Utility For Uploading Packages To PyPi",
            long_description=README,
            long_description_content_type="text/markdown",
            keywords=['gui', 'upload', 'pypi', 'twine', 'uploader', 'PyQt5'],
            url="https://github.com/360modder/up-to-pypi",
            author="360modder",
            author_email="apoorv9450@gmail.com",
            license="MIT",
            platforms=["Windows"],
            classifiers=[
                "License :: OSI Approved :: MIT License",
                "Programming Language :: Python :: 3.6",
                "Programming Language :: Python :: 3.7",
                "Programming Language :: Python :: 3.8",
            ],
            packages=["up_to_pypi"],
            package_data={'up_to_pypi':['*.pyw', 'assets/*ui','images/*.png','images/*.ico', 'assets/*.txt']},
            include_package_data=True,
            install_requires=["PyQt5==5.15.1", "qtmodern==0.2.0", "twine"],
            entry_points={
                "console_scripts": [
                    "up-to-pypi=up_to_pypi.launcher:main",
                    "awc=up_to_pypi.launcher:awc",
                    "crmod=up_to_pypi.launcher:crmod",
                ]
            },
        )
    else:
        print("Distributions Are Only Available For Windows . . .")
        exit()
