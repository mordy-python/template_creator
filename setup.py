import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Ashcodes", # Replace with your own username
    version="0.0.1",
    author="Mordy Waldner",
    author_email="imky171@gmail.com",
    description="A cli tool for creating basic flask apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mordy-python/template_creator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)