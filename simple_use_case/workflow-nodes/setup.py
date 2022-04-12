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
import os
from itertools import chain

from setuptools import find_packages
from setuptools import setup


with open(os.path.join("workflow_nodes", "version.py"), encoding="utf-8") as f:
    exec(f.read())


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


EXTRAS = {
    "ssh": [
        "paramiko<3.0.0",
        "scp<1.0.0",
    ],
}


setup(
    name="workflow-nodes",
    version=__version__,
    license="Apache-2.0",
    author="Karlsruhe Institute of Technology",
    description="Collection of tools for use in workflows.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/iam-cms/workflows/workflow-nodes",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6,<3.11",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "Click>=8.0.0,<9.0.0",
        "defusedxml<1.0.0",
        "graphviz<1.0.0",
        "kadi-apy>=0.21.0,<0.23.0",
        "matplotlib<4.0.0",
        "openpyxl<4.0.0",
        "pandas<2.0.0",
        "pylatex<2.0.0",
        "qrcode<8.0.0",
        "scipy>=1.5.1,<2.0.0",
        "xmlhelpy>=0.9.1,<1.0.0",
    ],
    extras_require={
        **EXTRAS,
        "all": [dep for dep in chain.from_iterable(EXTRAS.values())],
        "dev": [
            "beautifulsoup4==4.10.0",
            "black==22.3.0",
            "build==0.7.0",
            "jinja2==3.1.1",
            "pre-commit==2.17.0",
            "pylint==2.13.4",
            "recommonmark==0.7.1",
            "Sphinx==4.5.0",
            "sphinx_click==3.0.2",
            "sphinx-rtd-theme==1.0.0",
            "tox==3.24.5",
            "twine==4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "workflow-nodes=workflow_nodes.main:workflow_nodes",
        ]
    },
)
