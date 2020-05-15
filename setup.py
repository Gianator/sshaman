from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="sshaman",
    version="0.2.1",  # major.minor.bugfix,
    author="Gregory Clark",
    author_email="gianator@gianator.me",
    description="a simple ssh manager",
    packages=find_packages(),
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        sshaman=sshaman.__main__:sshaman
    ''',
    license="GPL-3.0",
    url="https://github.com/gianator/sshaman",
    long_description=open("README.md").read(),

)
