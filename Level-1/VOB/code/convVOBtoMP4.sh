#!/bin/bash
# run this command in code directory.
[ -d "../input" ] || {
    echo "Expecting input files  with vob format in code/../input directory with following structure:"
    echo "Please provide input"
    exit
}

[ -d "../output/" ] || { 
	echo "Creating code/../output directory to write final file there"
	mkdir ../output 
}

if [ ! -z "$1" -a "$1"!=" " ] 
then
	ffmpeg -i $1 "../output/archive.mp4" || echo "Please provide .vob file path as first argument"
else
	echo "Wrong input file provided. Pelase provide .vob file as first argument"
fi

