from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='pyComplexity',
    version='0.1.0',
    url='https://github.com/nickago/pyComplexity',
    author='nickago',
    author_email='ngonella@calpoly.edu',
    description='Python wrapper for GNU complexity that generates score reports on a traunch-based hierarchy of student turnins',
    long_description=readme,
    packages=['pyComplexity'],
    entry_points={
        'console_scripts': [
            'pyComplexity = pyComplexity.walkFile:main',
        ],
    },
    keywords=['pyComplexity'],
)
