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
from xmlhelpy import option

from .main import system


@system.command()
@option("file", description="file")
@option("interactive", char="i", description="Force interactive mode.", is_flag=True)
@option(
    "mathlib", char="l", description="Define the standard math library.", is_flag=True
)
@option(
    "warn",
    char="w",
    description="Give warnings for extensions to POSIX bc.",
    is_flag=True,
)
@option(
    "standard",
    char="s",
    description="Process exactly the POSIX bc language.",
    is_flag=True,
)
@option(
    "quiet",
    char="q",
    description="Do not print the normal GNU bc welcome.",
    is_flag=False,
)
def bc(file, interactive, mathlib, warn, standard, quiet):
    """Wrapper node for bc."""
    cmd = ["bc"]
    flags_str = "-"

    if interactive:
        flags_str += "i"
    if mathlib:
        flags_str += "l"
    if warn:
        flags_str += "w"
    if standard:
        flags_str += "s"
    if quiet:
        flags_str += "q"

    if len(flags_str) > 1:
        cmd += flags_str
    if file and file is not None:
        cmd += file

    # Do not write to stdout to keep output intact for piping.
    click.echo(" ".join(cmd), err=True)
    sys.exit(subprocess.run(cmd).returncode)
