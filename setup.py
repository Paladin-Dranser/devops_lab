import setuptools

setuptools.setup(
    name="monitoring",
    version="1.0",
    author="Antoś Bućko",
    author_email="anton_butsko@epam.com",
    description="Monitoring package",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux distros",
    ],
)
