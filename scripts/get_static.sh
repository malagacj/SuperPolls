#! /bin/bash

# Variables definition
root_folder=$(dirname $(dirname $(realpath $0)))
project_name=`basename $root_folder`

function download_zip {
	local url filename
	url=$1
	filename=$2

  rm -rf $filename
  wget -O $filename.zip $url
  unzip -d $filename $filename.zip; rm $filename.zip
  old_filename=`ls $filename`
  mv $filename/$old_filename/* $filename
  rm -rf $filename/$old_filename
}

# Starting script
cd $root_folder

if [ ! -d $project_name/static ]; then
	mkdir $project_name/static
fi

cd $project_name/static


## Bootstrap5
URL="https://github.com/twbs/bootstrap/releases/download/v5.2.3/bootstrap-5.2.3-dist.zip"
FILENAME="bootstrap5"
download_zip $URL $FILENAME
