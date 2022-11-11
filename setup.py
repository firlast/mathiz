from setuptools import setup

with open('README.md', 'r') as reader:
    readme = reader.read()

setup(
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    name='mathiz',
    description='Mathiz, a complete web framework',
    long_description=readme,
    long_description_content_type='text/markdown',
    version='0.1.0',
    url='https://github.com/firlast/mathiz',
    packages=['mathiz'],
    install_requires=['wsblib==0.4.0']
)