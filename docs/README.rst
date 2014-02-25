helpy
========

Description
-------------

``helpy`` displays built-in Python documentation from the command line without the need to use the interactive Python interpreter console. View documentation by Python module, class, method, function, or keyword.

Tested in cPython 2.6, 2.7, 3.2, 3.3, and pypy 2.2 (Python 2.7.3)

Install
---------

Install with ``pip`` using the command:

.. code-block:: bash

	pip install helpy

or download the source repository, unpack it, and navigate to the top level of the repository.  Then enter:

.. code-block:: bash

	python setup.py install

Usage
---------

.. code-block:: bash

	helpy <module,class,method,function,keyword>


Examples
-----------

Module Documentation
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

	helpy sys

Class Documentation
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

	helpy dict


Method Documentation
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

	helpy dict.update


Function Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

	helpy max


Issue Reporting
-------------------

Issue reporting is available on the `GitHub repository <https://github.com/chrissimpkins/helpy/issues>`_

