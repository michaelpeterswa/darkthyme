import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="darkthyme",
    version="1.0.2",
    author="Michael Peters",
    author_email="michael@michaelpeterswa.com",
    description="A time based cache for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michaelpeterswa/darkthyme",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
