#!/bin/bash
script_path="$(readlink -f "$0")"
script_dir="$(dirname "$script_path")"
project_folder="$(dirname "$script_dir")"

rm $project_folder/data/raw_data/*
rm $project_folder/data/processed_data/*
rm $project_folder/logs/*
rmdir $project_folder/logs
rm $project_folder/metrics/*
rm $project_folder/models/*
