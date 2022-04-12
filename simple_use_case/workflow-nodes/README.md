# workflow-nodes

**workflow-nodes** is a collection of tools written in Python 3, which are
usable inside a *workflow* as nodes. Each node is an executable command line
tool providing the `--xmlhelp` interface, which can be used to obtain a machine
readable representation of any command line tool and its parameters (see also
[xmlhelpy](https://gitlab.com/iam-cms/workflows/xmlhelpy)).

There are nodes for many different tasks, including data conversion, transport
and visualization tools.

## Installation

Install and update using [pip](https://pip.pypa.io/en/stable/getting-started/):

`pip3 install workflow-nodes -U`

Note that Python version >=3.6 is required.

Some tools require additional dependencies which are not installed by default,
as they might require additional setup which can vary for each operating
system. These dependencies can be installed by using the extras notation of
pip, e.g.:

`pip3 install workflow-nodes[<extra>]`

Please see the documentation for a list of extra dependencies. If desired, all
optional dependencies can also be installed at once using:

`pip3 install workflow-nodes[all]`

## Usage

In order to use a tool, make sure the `workflow-node` command is runnable from
anywhere, please see the documentation for more information. All tools are
grouped in different subcommands. To get more information or to get a list of
subcommands, the following commands can be used:

```
workflow-nodes --help
workflow-nodes --commands
```

To use the tools inside a workflow using `kadistudio`, they have to be added to
the file `$HOME/.kadistudio/tools.txt`. Afterwards you can insert them using
the "Add Tool" context menu option in the editor.

To register all available nodes from this repository at once, use the following
command:

`workflow-nodes --commands >> ~/.kadistudio/tools.txt`

## Development

When installing the library from source for development, it is recommended to
install the library in editable mode, which simply creates a link to the
sources so all changes are reflected in the installed package immediately.

`pip3 install -e .[dev]`

The command will also install some additional development dependencies as
defined in `setup.py`. Especially for development, it is highly recommended to
use a virtual environment, see
[Virtualenv](https://virtualenv.pypa.io/en/latest/ "Virtualenv") for more
information.

In order to add a new tool, please take a look at the following steps:

* First, create a fork of this project and clone it. The main repository can be
  added as an additional remote to the cloned project, often called `upstream`.
  Also checkout the `development` branch, which is currently used as the main
  development branch.
* Setup the [pre-commit](https://pre-commit.com/) hooks by running `pre-commit
  install`.
* Create a Python file for the tool in the desired package, e.g. in
  `workflow_nodes/report/` and implement the functionality of the tool. You can
  use other existing tools as a reference. Afterwards, add the implemented
  function to a fitting subcommand group, e.g. to
  `workflow_nodes/report/main.py`.
* If there are any new dependencies, add them to `setup.py` with appropriate
  version ranges, if necessary.
* Add an entry about any new functionality to `HISTORY.md`. You may also add
  yourself as a contributor to `AUTHORS.md`.
* Before creating a merge request on the main repository, make sure the GitLab
  CI runs through successfully in your fork.

## Further links

* Source code: https://gitlab.com/iam-cms/workflows/workflow-nodes
* Releases: https://pypi.org/project/workflow-nodes/
* Documentation:
  * Stable (reflecting the latest release):
    https://workflow-nodes.readthedocs.io/en/stable/
  * Latest (reflecting the *develop* branch):
    https://workflow-nodes.readthedocs.io/en/latest/
