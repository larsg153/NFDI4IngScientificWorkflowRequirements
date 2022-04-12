.. _setup-installation:

Installation
============

The library can be installed using ``pip3`` (or ``pip``, if there is no dedicated
version of ``pip`` for Python 3 installed), which generally comes bundled with Python
installations. Python version >= 3.6 is required.

.. code-block:: shell

    $ pip3 install workflow-nodes

When installing the library from source for development instead, it is recommended to
install the library in editable mode, which simply creates a link to the sources so all
changes are reflected in the installed package immediately. The command will also
install some additional development dependencies as defined in ``setup.py``.

.. code-block:: shell

    $ pip3 install -e .[dev]

Running the installations inside a virtual environment is recommended, see `Virtualenv
<https://virtualenv.pypa.io/en/latest/>`__ for more information.

Note that some tools require additional dependencies which are not installed by default,
as they might require additional setup which can vary for each operating system. These
dependencies can be installed by using the extras notation of pip, e.g.:

.. code-block:: shell

    $ pip3 install workflow-nodes[<extra>]

The following extras currently exist:

* ``ssh``: For using SSH tools via `Paramiko <https://www.paramiko.org/>`__.

If desired, all optional dependencies can also be installed at once using:

.. code-block:: shell

    $ pip3 install workflow-nodes[all]

In order to use a tool, make sure the ``workflow-node`` command is runnable from
anywhere. Depending on the type of installation and if a virtual environment is used or
not, the ``PATH`` system variable may need to be adapted accordingly to include the path
the executable resides in. For example, the following command can be used on Linux,
assuming the executable resides in ``~/.local/bin``:

.. code-block:: shell

  $ export PATH=${HOME}/.local/bin:${PATH}

This line can also be added to ``.bashrc`` so it will be executed each time a new
terminal is opened:

.. code-block:: shell

  $ echo 'export PATH=${HOME}/.local/bin:${PATH}' >> ${HOME}/.bashrc

On Windows, the ``PATH`` can be modified permanently by editing the respective
environment variable in the advanced system settings of the control panel.

To use the tools inside a workflow using ``kadistudio``, they have to be added to the
file ``$HOME/.kadistudio/tools.txt``. Afterwards you can insert them using the "Add
Tool" context menu option in the editor.

To register all available nodes from this repository at once, use the following
command:

.. code-block:: shell

    $ workflow-nodes --commands >> ~/.kadistudio/tools.txt

Autocompletion is also available for some shells, namely ``bash``, ``zsh`` and ``fish``,
and can be activated using:

.. code-block:: shell

    $ workflow-nodes config activate-autocompletion
