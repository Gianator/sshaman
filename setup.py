from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "sshaman",
    version = "0.1.0", # major.minor.bugfix,
    author = "Gregory Clark",
    author_email = "gianator@gianator.me",
    description = "a simple ssh manager",
    install_requires = requirements

    license = "GPL-3.0",
    url = "https://github.com/gianator/sshaman",
    long_description = open("README").read(),

)
