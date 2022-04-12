# Copyright 2020 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import subprocess
import sys

import click
from xmlhelpy import argument
from xmlhelpy import option

from .main import wsl


@wsl.command()
@argument(
    "arg0",
    description="Runnable file, must be specified using an absolute windows path (e.g."
    " C:\\Users\\user\\Documents\\example.bat) and will be given to the interpreter as"
    " is",
)
@option(
    "arguments",
    char="a",
    description="Arguments to run the shell script with. Separate multiple arguments"
    " with spaces",
)
@option(
    "interpreter",
    char="i",
    description="Overwrites the interpreter (default: Path to cmd.exe). Please specify"
    " an absolute unix path to any interpreter accepting a runnable file with the"
    ' option "/C". It must be reachable from within the WSL shell.',
    default="/mnt/c/Windows/System32/cmd.exe",
)
def win_shell_run(arg0, arguments, interpreter):
    """Run scripts or files using CMD or some other interpreter from within WSL."""
    click.echo(f"Running {arg0}...", err=True)
    cmd = [interpreter, "/C", arg0]

    if arguments:
        cmd += arguments.split(" ")

    cmd_str = " ".join(cmd)
    click.echo(f"Command: {cmd_str}", err=True)
    sys.exit(subprocess.run(cmd).returncode)
