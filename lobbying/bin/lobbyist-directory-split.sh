#!/bin/bash

commandpath=$(which pdftotext)

if [ -z "$commandpath" ];
then
echo "pdftotext not found on path, please install."
exit 0;
fi

function directory-split-left() {
    if [ "$#" -ne 2 ];
    then
    echo "You must enter exactly 2 command line arguments"
    else
    inputfile=$1
    outputfile=$2
    pdftotext -x 1 -y 1 -W 200 -H 570 -layout -f 1 -l 1 $inputfile $outputfile
    fi
}

function directory-split-right() {
    if [ "$#" -ne 2 ];
    then
    echo "You must enter exactly 2 command line arguments"
    else
    inputfile=$1
    outputfile=$2
    pdftotext -x 210 -y 1 -W 200 -H 570 -layout -f 1 -l 1 $inputfile $outputfile
    fi
}

export -f directory-split-left
export -f directory-split-right
