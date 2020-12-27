import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Python_CICD-Jhiggin", # Replace with your own username
    version="0.0.1",
    author="Joshua Higginbotham",
    author_email="joshua.higginbotham@codenamesql.com",
    description="A small example package for CICD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jhiggin/Python_CICD",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)