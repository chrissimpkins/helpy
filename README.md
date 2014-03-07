helpy   [![PyPI version](https://badge.fury.io/py/helpy.png)](https://pypi.python.org/pypi/helpy)
=======

#### Python Built-In Help Documentation from the Command Line

### Description

`helpy` displays built-in Python documentation from the command line without the need to use the interactive Python interpreter console. View documentation by Python module, class, method, function, or keyword.

Tested in cPython 2.6, 2.7, 3.2, 3.3, and pypy 2.2 (Python 2.7.3).  Documentation is from the Python interpreter version that is used to execute `helpy`

### Install

Install with `pip` by entering the following command:

``` bash
pip install helpy
```

or download and unpack the source repository, navigate to the top level directory in the repository, and enter:

``` bash
python setup.py install
```

### Usage

``` bash
helpy <module,class,method,function,keyword>
```

### Examples

#### Module Documentation

``` bash
$ helpy sys

Help on built-in module sys:

NAME
    sys

FILE
    (built-in)

MODULE DOCS
    http://docs.python.org/library/sys

DESCRIPTION
    This module provides access to some objects used or maintained by the
    interpreter and to functions that interact strongly with the interpreter.

    Dynamic objects:

...
```

#### Class Documentation

``` bash
$ helpy dict

Help on class dict in module __builtin__:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |
 |  Methods defined here:

 ...
```

#### Method Documentation

``` bash
$ helpy dict.update

Help on method_descriptor in dict:

dict.update = update(...)
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
    If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
    In either case, this is followed by: for k in F: D[k] = F[k]
```

#### Function Documentation

``` bash
$ helpy max

Help on built-in function max in module __builtin__:

max(...)
    max(iterable[, key=func]) -> value
    max(a, b, c, ...[, key=func]) -> value

    With a single iterable argument, return its largest item.
    With two or more arguments, return the largest argument.
```

### Issue Reporting

Issue reporting is available on the [GitHub repository](https://github.com/chrissimpkins/helpy/issues).


### Changes

1.0.1 - refactored help request code

1.0.0 - initial release


### License

[MIT License](https://github.com/chrissimpkins/helpy/blob/master/docs/LICENSE)
