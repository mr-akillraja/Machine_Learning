from setuptools import find_packages,setup

def get_requirements(file_path):
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup = (
    name = "ml_project",
    version = '0.0.1',
    author = "Sudharson",
    author_email = "mrakillraja@gmail.com "
    packages = find_package(),
    install_requirements = ['pandas','numpy','seaborn'],
)
