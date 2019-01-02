import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redash-query-download",
    version="0.0.1",
    author="Michihito Shigemura",
    author_email="i.am.shige@gmail.com",
    description="redash query download client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shigemk2/redash-query-download",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
