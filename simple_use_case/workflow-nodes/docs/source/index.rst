Welcome to workflow-nodes's documentation!
==========================================

|pypi| |license| |zenodo|

.. |pypi| image:: https://img.shields.io/pypi/v/workflow-nodes
    :target: https://pypi.org/project/workflow-nodes/
    :alt: PyPi

.. |license| image:: https://img.shields.io/pypi/l/workflow-nodes
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: License

.. |zenodo| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.4094718.svg
    :target: https://doi.org/10.5281/zenodo.4094718
    :alt: Zenodo

**workflow-nodes** is a collection of tools written in Python 3, which are usable inside
a *workflow* as nodes. Each node is an executable command line tool providing the
``--xmlhelp`` interface, which can be used to obtain a machine readable representation
of any command line tool and its parameters (see also `xmlhelpy
<https://gitlab.com/iam-cms/workflows/xmlhelpy>`__).

There are nodes for many different tasks, including data conversion, transport
and visualization tools.

.. toctree::
    :name: setup
    :caption: Setup
    :maxdepth: 1

    setup/installation
    setup/upgrade
    setup/configuration

This sections describes how to install, upgrade and configure the workflow-nodes.

.. toctree::
    :name: usage
    :caption: Usage
    :maxdepth: 1

    usage/cli

This section describes all available tools.

.. toctree::
    :name: release-history
    :caption: Release history
    :maxdepth: 2

    HISTORY.md
