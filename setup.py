from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

is_local_env = False
if "APP_ENV" in os.environ:
    is_local_env = os.environ["APP_ENV"] == "local"

project_name = 'devpair'
if is_local_env:
    project_name='localdevpair'

setup(
    name=project_name,
    version='1.0.1',
    author='Raphael Kieling',
    author_email='raphaelkieling98@gmail.com',
    description='Pair script that manage a pair programming session using git.',
    license='MIT',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[requirements],
    python_requires='>=3.5',
    py_modules=[project_name, 'app'],
    entry_points=f'''
        [console_scripts]
        {project_name}={project_name}:exec_cli
    '''
)
