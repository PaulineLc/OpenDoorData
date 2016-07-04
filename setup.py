import os
import pip

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages
    
#requirements = pip.req.parse_requirements('requirements.txt')

requirements = []
for i in pip.get_installed_distributions(local_only=True):
    requirements.append(str(i))


setup(
  name='Tech-Quartet',
  version='0.1.0',
  description='UCD Summer research project',
  url='',
  license='MIT',
  author='',
  author_email='',
  packages=find_packages(exclude=['tests*']),
  install_requires= requirements,
  include_package_data=True,
  entry_points = {
  'console_scripts': ["",
  ]
  },

)