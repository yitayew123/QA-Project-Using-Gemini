# Import functions from setuptools to help package and distribute Python projects
from setuptools import find_packages, setup  

# Use the setup() function to define the Python package metadata and configuration
setup(
    # Name of the package
    name='QApplication',  
    
    # Version of the package
    version='0.0.1',  
    
    # Author name
    author='Yitayew Solomon',  
    
    # Author email
    author_email='yitayewsolomon3@gmail.com',  
    
    # Automatically find all Python packages (directories with __init__.py) in the project
    packages=find_packages(),  
    
    # List of dependencies required to install this package
    # Currently empty, but you can add packages like ['numpy', 'pandas'] here
    install_requires=[]
)
