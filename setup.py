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
            version="1.0.9",
            description="A PyQt5 GUI Uploder For Uploading Packages To PyPi",
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
            package_data={'up_to_pypi':['*.pyw', '*.exe', 'assets/*ui','images/*.png','images/*.ico', 'assets/*.txt']},
            include_package_data=True,
            install_requires=["twine", "jinja2"],
            entry_points={
                "console_scripts": [
                    "up-to-pypi=up_to_pypi.launcher:main",
                    "uptopypi=up_to_pypi.launcher:main",
                    "up_to_pypi=up_to_pypi.launcher:main",
                ]
            },
        )
    else:
        print("Distributions Are Only Available For Windows . . .")
        print("But You Can Port It To Any Platform . . .\n")
        print("View At :\nhttps://github.com/360modder/up-to-pypi/blob/main/up_to_pypi/main.pyw")
        exit()
