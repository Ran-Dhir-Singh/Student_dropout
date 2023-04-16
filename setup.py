from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    returns the list of requirements from the requirements.txt file
    """
    HYPHEN_E_DOT = '-e .'   # creating an `-e .` variable to skip it from requirements list 
    requirements =[]        # Initializing an empty list to store the requirement packages

    # Read the requiremnts.txt file and add it to requirements list
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]       #replacing  \n with empty space

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name = 'Student_dropout',
    version = '0.0.1',
    author = 'Randhir Singh',
    author_email = 'randhirsingh7777777@gmail.com',
    description = 'ML classification project to predict if a student will dropout or not',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)
