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
import re

import click
from docutils import nodes
from docutils import statemachine
from sphinx.util import nodes as sphinx_nodes
from sphinx_click.ext import _filter_commands
from sphinx_click.ext import _format_arguments
from sphinx_click.ext import _format_description
from sphinx_click.ext import _format_envvars
from sphinx_click.ext import _format_epilog
from sphinx_click.ext import _format_subcommand
from sphinx_click.ext import _format_usage
from sphinx_click.ext import _get_help_record
from sphinx_click.ext import _indent
from sphinx_click.ext import ClickDirective


# pylint: disable=missing-function-docstring


# The following code is a slightly modified version of sphinx_clicks's click directive
# and helper functions, which are available at the following URL:
# https://github.com/click-contrib/sphinx-click/tree/2.7.1
#
# sphinx_click is licensed under the MIT license:
#
# The MIT License
#
# Copyright (c) 2017 Stephen Finucane http://that.guru/
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


NESTED_FULL = "full"
NESTED_NONE = "none"

ANSI_ESC_SEQ_RE = re.compile(r"\x1B\[\d+(;\d+){0,2}m", flags=re.MULTILINE)

EXCLUDED_OPTIONS = ["verbose", "version", "xmlhelp"]

ESCAPED_SYMBOLS = ["*"]


def _escape_string(value):
    for symbol in ESCAPED_SYMBOLS:
        value = value.replace(symbol, f"\\{symbol}")

    return value


def _get_help_record(opt):
    def _write_opts(opts):
        rv, _ = click.formatting.join_options(opts)
        if not opt.is_flag and not opt.count:
            name = opt.name
            if opt.metavar:
                name = opt.metavar.lstrip("<[{($").rstrip(">]})$")
            rv += f" <{name}>"
        return rv

    rv = [_write_opts(opt.opts)]
    if opt.secondary_opts:
        rv.append(_write_opts(opt.secondary_opts))

    out = []
    if opt.help:
        if opt.required:
            out.append(f"**Required** {_escape_string(opt.help)}")
        else:
            out.append(_escape_string(opt.help))
    else:
        if opt.required:
            out.append("**Required**")

    extras = []

    if opt.default is not None and opt.show_default:
        if isinstance(opt.show_default, str):
            # This can be a string as well. This is mostly useful when the default is
            # not a constant and documentation thus needs a manually written string.
            extras.append(f":default: {_escape_string(opt.show_default)}")
        else:
            default_value = _escape_string(
                ", ".join(str(d) for d in opt.default)
                if isinstance(opt.default, (list, tuple))
                else str(opt.default)
            )
            extras.append(f":default: {default_value}")

    if isinstance(opt.type, click.Choice):
        choice_values = " | ".join(str(x) for x in opt.type.choices)
        extras.append(f":options: {choice_values}")

    if extras:
        if out:
            out.append("")

        out.extend(extras)

    return ", ".join(rv), "\n".join(out)


def _format_option(opt):
    opt = _get_help_record(opt)

    yield f".. option:: {opt[0]}"
    if opt[1]:
        yield ""
        for line in statemachine.string2lines(
            ANSI_ESC_SEQ_RE.sub("", opt[1]), tab_width=4, convert_whitespace=True
        ):
            yield _indent(line)


def _format_options(ctx):
    params = [
        param
        for param in ctx.command.params
        if isinstance(param, click.Option) and not param.hidden
    ]

    for param in params:
        if param.name in EXCLUDED_OPTIONS:
            continue

        yield from _format_option(param)
        yield ""


def _format_command(ctx, nested, commands=None):
    if ctx.command.hidden:
        return

    yield from _format_description(ctx)

    yield f".. program:: {ctx.command_path}"

    yield from _format_usage(ctx)

    lines = list(_format_options(ctx))
    if lines:
        # we use rubric to provide some separation without exploding the table of
        # contents
        yield ".. rubric:: Options"
        yield ""

    yield from lines

    lines = list(_format_arguments(ctx))
    if lines:
        yield ".. rubric:: Arguments"
        yield ""

    yield from lines

    lines = list(_format_envvars(ctx))
    if lines:
        yield ".. rubric:: Environment variables"
        yield ""

    yield from lines

    yield from _format_epilog(ctx)

    # if we're nesting commands, we need to do this slightly differently
    if nested in (NESTED_FULL, NESTED_NONE):
        return

    commands = _filter_commands(ctx, commands)

    if commands:
        yield ".. rubric:: Commands"
        yield ""

    for command in commands:
        # Don't show hidden subcommands
        if command.hidden:
            continue

        yield from _format_subcommand(command)
        yield ""


class Click(ClickDirective):
    """Modified ``click`` directive.

    Ignores some common options and automatically escapes descriptions and default
    values of the parameters.
    """

    def _generate_nodes(
        self, name, command, parent, nested, commands=None, semantic_group=False
    ):
        ctx = click.Context(command, info_name=name, parent=parent)

        if command.hidden:
            return []

        # Title
        section = nodes.section(
            "",
            nodes.title(text=name),
            ids=[nodes.make_id(ctx.command_path)],
            names=[nodes.fully_normalize_name(ctx.command_path)],
        )

        # Summary
        source_name = ctx.command_path
        result = statemachine.ViewList()

        if semantic_group:
            lines = _format_description(ctx)
        else:
            lines = _format_command(ctx, nested, commands)

        for line in lines:
            result.append(line, source_name)

        sphinx_nodes.nested_parse_with_titles(self.state, result, section)

        # Subcommands
        if nested == NESTED_FULL:
            if isinstance(command, click.CommandCollection):
                for source in command.sources:
                    section.extend(
                        self._generate_nodes(
                            source.name,
                            source,
                            parent=ctx,
                            nested=nested,
                            semantic_group=True,
                        )
                    )
            else:
                commands = _filter_commands(ctx, commands)
                for cmd in commands:
                    parent = ctx if not semantic_group else ctx.parent
                    section.extend(
                        self._generate_nodes(
                            cmd.name, cmd, parent=parent, nested=nested
                        )
                    )

        return [section]


def setup(app):
    app.add_directive("click", Click)
