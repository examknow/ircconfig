import setuptools

with open("VERSION", "r") as f:
    version = f.read().strip()

setuptools.setup(
    name="ircconfig",
    version=version,
    author="examknow",
    author_email="me@zpld.me",
    description="Library for generic irc bot configuration",
    url="https://github.com/examknow/ircconfig",
    packages=setuptools.find_packages(),
    package_data={"ircconfig": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows"
    ],
    python_requires='>=3.6',
)
