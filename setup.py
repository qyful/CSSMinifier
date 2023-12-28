from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Minification tool for Cascading Style Sheets (CSS)'
LONG_DESCRIPTION = 'An open source Python minification package for Cascading Style Sheets (CSS).'

setup(
        name="cssminifier", 
        version=VERSION,
        author="Oliwier Sporny",
        author_email="me@oliwiersporny.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 4 - Beta",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)