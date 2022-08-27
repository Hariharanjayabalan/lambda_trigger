#!/bin/bash
declare -a folder_name=('github_archive')
rm -rf lambda_zip
rm -rf comman_zip
mkdir lambda_zip
mkdir comman_zip
pip install -r requirements.txt -t comman_zip
for pkg in ${folder_name[@]}
do 
echo $pkg
zip -rq lambda_zip/upload.zip $pkg
cd comman_zip
zip -rq ../lambda_zip/upload.zip .
done
rm -rf ../comman_zip