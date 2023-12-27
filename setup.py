from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Minification tool for Cascading Style Sheets (CSS)'
LONG_DESCRIPTION = 'A Python open source minification tool for Cascading Style Sheets (CSS).'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="verysimplemodule", 
        version=VERSION,
        author="Oliwier Sporny",
        author_email="me@oliwiersporny.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)