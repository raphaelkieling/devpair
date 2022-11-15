from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='devpair',
    version='1.0',
    author='Raphael Kieling',
    author_email='raphaelkieling98@gmail.com',
    description='Pair script that manage a pair programming session using git.',
    license='MIT',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[requirements],
    python_requires='>=3.5',
    py_modules=['devpair', 'app'],
    entry_points='''
        [console_scripts]
        devpair=devpair:exec_cli
    '''
)
