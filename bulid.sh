#!/bin/bash
echo 'Hari testing'
#declare -a folder_name=('github_archive')
folder_name='github_archive'
rm -rf lambda_zip
rm -rf comman_zip
mkdir lambda_zip
mkdir comman_zip
pip install -r requirements.txt -t comman_zip
zip -rq lambda_zip/upload.zip $folder_name
cd comman_zip
zip -rq ../lambda_zip/upload.zip .
rm -rf ../comman_zip