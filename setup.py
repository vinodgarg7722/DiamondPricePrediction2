from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        return requirements

setup(

    name='DiamondPricePrediction',
    version='0.0.1',
    author='vinod',
    author_email='vinodgarg070702@gmail.com',
    # install_requires=['pandas','numpy']
    install_requires=get_requirements('requirements.txt'),


    packages=find_packages()
)