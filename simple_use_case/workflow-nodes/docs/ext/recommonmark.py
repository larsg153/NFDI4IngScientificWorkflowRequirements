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
from recommonmark.parser import CommonMarkParser as _CommonMarkParser


# pylint: disable=missing-function-docstring


class CommonMarkParser(_CommonMarkParser):
    """Modified Markdown parser.

    Workaround in order to suppress a user warning caused by not overriding the method
    below.
    """

    def visit_document(self, node):
        pass


def setup(app):
    app.add_source_parser(CommonMarkParser)
    app.add_source_suffix(".md", "markdown")
