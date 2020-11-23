import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="catmux",
    version="0.1.0",
    author="Felix Exner",
    author_email="felix_mauch@web.de",
    description="Catmux is package to enable the user to start a tmux session with multiple windows and splits with ease.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fmauch/catmux",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['script/create_session']
)
