<pre>

 ██████╗███████╗███████╗███╗   ███╗██╗███╗   ██╗██╗███████╗██╗███████╗██████╗ 
██╔════╝██╔════╝██╔════╝████╗ ████║██║████╗  ██║██║██╔════╝██║██╔════╝██╔══██╗
██║     ███████╗███████╗██╔████╔██║██║██╔██╗ ██║██║█████╗  ██║█████╗  ██████╔╝
██║     ╚════██║╚════██║██║╚██╔╝██║██║██║╚██╗██║██║██╔══╝  ██║██╔══╝  ██╔══██╗
╚██████╗███████║███████║██║ ╚═╝ ██║██║██║ ╚████║██║██║     ██║███████╗██║  ██║
 ╚═════╝╚══════╝╚══════╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                              
------------------------------------------------------------------------------

                   An open source Python minification package
                       for Cascading Style Sheets (CSS).
</pre>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cssminifier)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/cssminifier)

<div>

## Installation & Basic Usage
To install the package, you should use the PIP package manager:

```
pip install cssminifier
```

After that, you can import it into a Python script and use it as you desire. For example:

```py
from cssminifier import Minifier

def main():
    with open("tests/media_queries.css", 'r') as fp:
        minifier = Minifier(fp.read())

        print(minifier())
        
        fp.close()

if __name__ == '__main__':
    main()
```