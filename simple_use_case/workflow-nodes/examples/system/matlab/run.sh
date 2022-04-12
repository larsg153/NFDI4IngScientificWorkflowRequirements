#!/usr/bin/env bash
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
current_dir=$(dirname $(readlink -f $0))

# Path of Matlab file
path="${current_dir}/files"
# Matlab file to read
file="WrapperTest"

# Choose execution mode
emode="single"
# emode="bash"
# emode="desktop"

# Execute Matlab file
workflow-nodes system matlab $file -f $path -m $emode
