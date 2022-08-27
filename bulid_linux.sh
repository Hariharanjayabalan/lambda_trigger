#!/bin/bash
echo "Starting the Script"
declare -a folder_name=('github_archive')
echo "Removing the previous bulid"
rm -rf lambda_zip
rm -rf comman_zip
mkdir lambda_zip
mkdir comman_zip
echo "Running Requirement file"
pip install -r requirements_for_bulid.txt -t comman_zip
for pkg in ${folder_name[@]}
do 
echo "Running Zip process"
zip -rq lambda_zip/upload.zip $pkg
cd comman_zip
zip -rq ../lambda_zip/upload.zip .
done
rm -rf ../comman_zip