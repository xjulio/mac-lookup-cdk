import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="mac_lookup_cdk",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "mac_lookup_cdk"},
    packages=setuptools.find_packages(where="mac_lookup_cdk"),

    install_requires=[
        "aws-cdk-lib==2.0.0-rc.1",
        "constructs>=10.0.0,<11.0.0",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
