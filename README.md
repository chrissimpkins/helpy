pyh
=====

#### Python Built-In Help Documentation from the Command Line

### Description

pyh displays built-in Python documentation from the command line without the need to use the interactive Python interpreter console. View documentation by Python module, class, method, function, or keyword.

### Install

Install with `pip` by entering the following command:

``` bash
pip install pyh
```

or download and unpack the source repository, navigate to the top level directory in the repository, and enter:

``` bash
python setup.py install
```

### Usage

``` bash
pyh <module,class,method,function,keyword>
```

### Examples

#### Module Documentation

``` bash
pyh sys
```

#### Class Documentation

``` bash
pyh dict
```

#### Method Documentation

``` bash
pyh dict.update
```

#### Function Documentation

``` bash
pyh max
```

### Issue Reporting

Issue reporting is available on the [GitHub repository](https://github.com/chrissimpkins/pyh/issues).
