import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DynaTMT", 
    version="2.9.3",
    author="Süleyman Bozkurt",
    author_email="Bozkurt@med.uni-frankfurt.de",
    # Updated by = "Süleyman Bozkurt",
    # Updated date = '18/03/2026'
    description="Python package to analyse pSILAC TMT data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/science64/DynaTMT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)