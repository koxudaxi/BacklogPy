====================================================
BacklogPy - Backlog API v2 Client Library for Python
====================================================


|Build Status| |Version|


BacklogPy is `Backlog API v2 <https://developer.nulab-inc.com/docs/backlog/>`_ Client Library for Python 2/3


.. |Build Status| image:: http://img.shields.io/travis/koxudaxi/BacklogPy/master.svg?style=flat
    :target: https://travis-ci.org/koxudaxi/BacklogPy
    :alt: Build Status
.. |Version| image:: http://img.shields.io/pypi/v/BacklogPy.svg?style=flat
    :target: https://pypi.python.org/pypi/BacklogPy/
    :alt: Version


Install
-------
You can install the client library with pip:

.. code-block:: sh

    $ pip install BacklogPy

Example
-------
The client Library has API Call methods for All Backlog v2 API:

.. code-block:: python

    >>> from BacklogPy import Backlog
    >>> backlog = Backlog('space_name','api-key')
    >>> response = backlog.get_project_list(all=True, archived=True)
    >>> print(response.json()[0])
       {'archived': False,
        'chartEnabled': True,
        'displayOrder': 1234563786,
        'id': 12345,
        'name': 'Coffee Project',
        'projectKey': 'COFFEE_PROJECT',
        'projectLeaderCanEditProjectLeader': True,
        'subtaskingEnabled': False,
        'textFormattingRule': 'markdown',
        'useWikiTreeView': True}



Also you can use dict parameters with '\*_raw' methods:

.. code-block:: python

    >>> response = backlog.get_project_list_raw({'archived':'false', 'all':'false'})


ScreenShot
----------

You can use auto-completion for methods and arguments in Interpreter(IPython) and IDE(PyCharm, Jedi and more)

.. image:: https://raw.githubusercontent.com/koxudaxi/BacklogPy/master/docs/img/auto-completion_arguments.png
.. image:: https://raw.githubusercontent.com/koxudaxi/BacklogPy/master/docs/img/auto-completion_method.png


Development
-----------

Tests
~~~~~
``tox`` can support to test with few python versions

.. code-block:: sh

    $ tox
    $ tox -e py26,py36

or ``nosetests`` for one Python version

.. code-block:: sh

    $ nosetests tests/backlog

Generating The Backlog API v2 Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Backlog API v2 Client is created by api_generator.
api_generator downloads API Documents from https://developer.nulab-inc.com/docs/backlog/ .
And parse API Documents to generate The Backlog API v2 Client:

.. code-block:: sh

    $ python3 api_generator/api_generator.py download
    $ python3 api_generator/api_generator.py create

Build Wheel Package
~~~~~~~~~~~~~~~~~~~

.. code-block:: sh

    $ pip3 install wheel
    $ python3 setup.py bdist_wheel
