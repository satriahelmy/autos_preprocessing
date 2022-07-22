import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = "autos-preprocessing",
    version = "0.0.1",
    author = "Helmy",
    autor_email = "helmysmp@gmail.com",
    description = "Simple Repos for Preprocessing Autos Data",
    long_description = "Simple Repos for Preprocessing Autos Data",
    long_description_content_type = "text/markdown",
    url = "",
    packages = setuptools.find_packages(),
    classifier = ["Programming Language :: Python :: 3"],
    install_requires = [
        "numpy",
        "pandas",
        "scikit-learn"],
    python_requires = ">=3.7"
)