from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Read the requirements from a file and return them as a list."""
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_lst

setup(
    name='NetworkSecuritySystem',
    author='Kiru',
    author_email='kirankumardhanireddy@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
