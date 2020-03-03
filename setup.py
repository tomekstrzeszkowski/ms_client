import setuptools
import os

base_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(base_dir, 'README.md')) as f:
        long_description = '\n{}'.format(f.read())

setuptools.setup(
    name="client", # Replace with your own username
    version="0.0.1",
    author="Tomasz Strzeszkowski",
    author_email="tomasz.Strzeszkowski@gmail.com.com",
    description="Client wrapper for MarketScan",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomekstrzeszkowski/ms_client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'requests',
   ]
)
