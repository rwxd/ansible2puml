from setuptools import setup, find_packages
from os import path

with open("./requirements.txt") as f:
    required = f.read().splitlines()

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='ansible2puml',
      version='0.3.1',
      description='Create an PlantUML Activity Diagram from Playbooks or Roles trough Python.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='profileid',
      author_email='profileid@protonmail.com',
      url="https://github.com/ProfileID/ansible2puml",
      license='MIT',
      packages=['ansible2puml'],
      install_requires=required,
      entry_points={
          "console_scripts": ["ansible2puml = ansible2puml.cli:main"]
      },
      classifiers=[
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8'
      ]
      )
