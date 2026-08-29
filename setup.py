#responsible for creating the machine learning app as a package
#from here anybody can use the installation

#find all the packages in the app

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        # Remove -e . if present (it won't be anymore)
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Ali',
    author_email='ali3lebanon@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
#uses __init__.py to consider the folder as a package

        