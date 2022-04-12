#!/usr/bin/env bash
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
current_dir=$(dirname $(readlink -f $0))

# Excel file to read
file="${current_dir}/files/test.xlsx"

# Define start and end column of records
colums_start=E
colums_end=F

# Upload all data for one record
workflow-nodes converter excel-to-kadi $file -S $colums_start -E $colums_end -b "${current_dir}/files/" -f
