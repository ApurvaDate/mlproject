from setuptools import find_packages , setup #find all the packages
from typing import List


def get_requirements (file_path:str)-> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()  #the line will get readed, but \n will get added
        requirements = [ req.replace("\n","") for req in requirements]  #replace \n with blank

        requirements = [req for req in requirements if not req.startswith('-e.')]

    return requirements

setup(
    name = "mlproject", 
    version = "0.0.1", 
    author= "apurva", 
    author_email= "apurvadate25@gmail.com",
    packages=find_packages(),
    # install_requires = ['pandas', 'numpy', 'seaborn '] #automatic installation can be done
    install_requires = get_requirements('requirements.txt'))
    