#!/bin/bash
script_path="$(readlink -f "$0")"
script_dir="$(dirname "$script_path")"
project_folder="$(dirname "$script_dir")"

source "$project_folder/env/bin/activate"
PYTHONPATH="$project_folder" python "$project_folder/src/data/pull_data.py"