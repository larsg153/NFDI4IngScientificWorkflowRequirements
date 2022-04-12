#!/usr/bin/env python3
# Copyright 2021 Karlsruhe Institute of Technology
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
import os
import subprocess
import sys
from datetime import datetime
from datetime import timezone

import bs4
import click
from jinja2 import Environment
from jinja2 import FileSystemLoader

from workflow_nodes.utils import check_binary


@click.command()
@click.argument("command", required=True)
@click.option(
    "-f",
    "--file",
    type=click.File("w"),
    default="-",
    help="Output file the workflow wrapper is saved in.",
)
@click.option(
    "-g",
    "--group",
    default="system",
    help="Click group the workflow wrapper will belong to.",
)
def create_node_template(command, file, group):
    """Tool for creating new workflow wrapper tools based on an existing program."""
    check_binary("help2man")
    check_binary("man2html")

    # pylint: disable=consider-using-with
    p1 = subprocess.Popen(["help2man", command], stdout=subprocess.PIPE)
    p2 = subprocess.Popen("man2html", stdin=p1.stdout, stdout=subprocess.PIPE)
    # Allow p1 to receive a SIGPIPE if p2 exits before p1.
    p1.stdout.close()
    output = p2.communicate()[0]
    p1.wait()

    if p1.returncode != 0 or p2.returncode != 0:
        sys.exit(1)

    html = output.decode()
    soup = bs4.BeautifulSoup(html, "lxml")

    html_list = [elem.strip() for elem in soup.get_text().splitlines() if elem.strip()]
    index = html_list.index("DESCRIPTION")
    description = html_list[index + 1]

    args = []
    args_dict = []
    for arg in soup.find_all("dl")[0].find_all("dt"):
        args_dict.append(
            {
                "char": None,
                "keyword": None,
                "description": None,
            }
        )
        for item in arg.find_all("b"):
            item_text = item.get_text()
            if item_text[0] == "-" and item_text[1] != "-":
                args_dict[-1]["char"] = item_text
            if item_text[0:2] == "--":
                args_dict[-1]["keyword"] = item_text

    for index, arg_description in enumerate(soup.find_all("dl")[0].find_all("dd")):
        args_dict[index]["description"] = " ".join(arg_description.get_text().split())

    args_dict = [
        arg
        for arg in args_dict
        if not (arg["keyword"] == "--help" or arg["keyword"] == "--version")
    ]

    for arg in args_dict:
        if arg["keyword"]:
            args.append(arg["keyword"][2:].replace("-", "_"))
        else:
            args.append(arg["char"][1:])

    args = ", ".join(args)

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(f"{os.path.dirname(__file__)}/templates/node.jinja")
    node = template.render(
        command=command,
        description=description,
        args_dict=args_dict,
        args=args,
        group=group,
        year=datetime.now(timezone.utc).year,
    )

    click.echo(node, file=file)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    create_node_template()
