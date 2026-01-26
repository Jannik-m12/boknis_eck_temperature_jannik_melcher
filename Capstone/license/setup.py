
# Source: 
# https://timeseries.geomar.de/boknis/app/
# https://www.geomar.de/zentrum/forschungsinfrastruktur/boknis-eck-zeitserienstation

# setup.py
from setuptools import setup, find_packages

setup(
    name="boknis-client",
    version="0.1.2",
    packages=find_packages(),
    install_requires=["requests", "pandas", "Pyarrow"],
    author="Claas Faber",
    author_email="cfaber@geomar.de",
    description="A python client for the Boknis Eck Timeseries Database",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
