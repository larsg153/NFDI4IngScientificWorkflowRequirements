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
from workflow_nodes.main import workflow_nodes


@workflow_nodes.group()
def misc():
    """Miscellaneous tools."""


# pylint: disable=unused-import


from .create_qr_code import create_qr_code
from .create_symlink import create_symlink
from .files_combine import files_combine
from .imagej_macro import imagej_macro
from .imagej_variable import imagej_variable
from .matlab import matlab
from .octave import octave
from .paraview_macro import paraview_macro
from .run_script import run_script
from .send_mail import send_mail
from .xmllint import xmllint
from .gmsh import gmsh
from .latexmk import latexmk
from .meshio_convert import meshio_convert
from .pvbatch import pvbatch
from .tectonic import tectonic
