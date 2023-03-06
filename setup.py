from setuptools import find_packages,setup

setup(
     name='ML_Project_003',
     version='0.0.1',
     author="Raja",
     author_email='maharengarajan46@gmail.com',
     packages=find_packages(),
     install_requires=get_requirements('requiremts.tst')

)