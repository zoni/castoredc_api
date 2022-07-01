from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="castoredc_api",
    version="0.1.4",
    description="Python wrapper for the Castor EDC API",
    author="Reinier van Linschoten",
    author_email="mail@reiniervl.com",
    maintaner="Reinier van Linschoten",
    maintaner_email="mail@reiniervl.com",
    url="https://github.com/reiniervlinschoten/castoredc_api",
    packages=find_packages(include=("castoredc_api", "castoredc_api.*")),
    install_requires=[
        "pandas>=1.3.1",
        "numpy>=1.21.1",
        "openpyxl>=3.0.7",
        "tqdm>=4.62.0",
        "httpx>=0.19.0",
        # importlib.metadata was only introduced in Python 3.8, but the
        # "importlib-metadata" package provides it for older Python versions.
        'importlib-metadata >= 1.0 ; python_version < "3.8"',
    ],
    tests_require=["pytest", "pytest-httpx"],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
