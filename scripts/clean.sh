#!/bin/bash
script_path="$(readlink -f "$0")"
script_dir="$(dirname "$script_path")"
project_folder="$(dirname "$script_dir")"

rm $project_folder/data/raw_data/*.csv
rm $project_folder/data/processed_data/*.csv
rm $project_folder/logs/*.txt
rmdir $project_folder/logs
rm $project_folder/metrics/*.json
rm $project_folder/models/*.pkl
