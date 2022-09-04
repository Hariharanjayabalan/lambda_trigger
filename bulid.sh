#!/bin/bash
echo "Starting the Script"
folder_name='github_archive'
echo "Removing the previous bulid"
rm -rf lambda_zip
rm -rf comman_zip
mkdir lambda_zip
mkdir comman_zip
echo "Running Requirement file"
pip install -r requirements_for_bulid.txt -t comman_zip
echo "Running Zip process"
zip -rq lambda_zip/github_archive.zip $folder_name
cd comman_zip
zip -rq ../lambda_zip/github_archive.zip .
rm -rf ../comman_zip