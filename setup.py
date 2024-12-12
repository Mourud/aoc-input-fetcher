import subprocess
from setuptools import setup, find_packages

cf_remote_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)
setup(
    name="aoc_input_fetcher",
    version=cf_remote_version,
    description="A useful tool for getting the input automatically for Advent of Code, given you follow the file structure",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mourud Ishmam Ahmed",
    author_email="ishmam1@gmail.com",
    url="https://github.com/mourud/aoc-input-fetcher",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/mourud/aoc-input-fetcher/issues",
        "Documentation": "https://github.com/mourud/aoc-input-fetcher#readme",
    },
    keywords=["Advent of Code", "input fetcher", "automation"],
)
