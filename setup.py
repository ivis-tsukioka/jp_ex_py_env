import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setuptools.setup(
    name="jp-ex-py-env",
    version="1.0.0",
    description="Some Platform metadata convert to RO-Crate",
    license='Apache License 2.0',
    author="NII",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NII-DG/dg-packager.git",
    python_requires=">=3.8",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    #install_requires=................ [TODO] Set up after nii-dg library is released

)