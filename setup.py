from setuptools import find_packages, setup
from typing import List

HYPHEN= "-e ."

def get_req(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN in requirements:
            requirements.remove(HYPHEN)
    return requirements
        
 

setup(

    name="StudentPerformanceInExam",
    version="0.0.1",
    author="saharatif",
    author_email="saharatif85@gmail.com",
    packages=find_packages(),
    install_requires = get_req("requirements.txt")
)