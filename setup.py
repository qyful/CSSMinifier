from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Minification tool for Cascading Style Sheets (CSS)'
LONG_DESCRIPTION = 'An open source Python minification package for Cascading Style Sheets (CSS).'

setup(
        name="cssminifier", 
        version=VERSION,
        license="MIT",
        author="Oliwier Sporny",
        author_email="me@oliwiersporny.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        keywords=["css", "css3", "minifier", "minification", "minify", "minify-css"],
        download_url='https://github.com/qyful/CSSMinifier/archive/refs/tags/v0.0.1.tar.gz',
        url="https://github.com/qyful/cssminifier",
        packages=find_packages(),
        install_requires=[], 
            classifiers= [
            "Development Status :: 4 - Beta",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)