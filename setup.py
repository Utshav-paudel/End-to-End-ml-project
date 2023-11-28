#@ Implementation of setup.py needed for creating pypi packages

from setuptools import find_packages,setup
from typing import List

# function that will return the list of all packages in requirements.txt to install_requires
def get_requirements(file_path:str)->List[str]:
    'will return the list of packages need to install and get called in hypen e dot in requirements.txt'

    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:                                 #  insatlling package through requirements.txt
            requirements.remove(HYPEN_E_DOT)       
    return requirements

setup(
    name = 'anime_recommender_webapp',
    version = '0.0.1',
    author = 'Utshav paudel',
    author_email = 'utshav.paudel466@gmail.com',
    install_requires = get_requirements('requirements.txt')
)