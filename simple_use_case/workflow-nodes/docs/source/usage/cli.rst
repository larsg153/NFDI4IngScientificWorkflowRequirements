.. _usage-cli:

CLI
===

While the tools of this library were created to be used within a *workflow*, all tools
can also be used directly in the terminal, inside a shell script or by running it as an
external command inside most programming languages. The first entry point to the CLI is
given by running:

.. code-block:: shell

    $ workflow-nodes

All tools are grouped in different subcommands. To get more information or to get a list
of subcommands, the following commands can be used:

.. code-block:: shell

    $ workflow-nodes --help
    $ workflow-nodes --commands

The information on how to run a certain tool can be accessed analogously, e.g.:

.. code-block:: shell

    $ workflow-nodes plot plot-matplotlib --help

.. toctree::
    :maxdepth: 3

    cli/tools
