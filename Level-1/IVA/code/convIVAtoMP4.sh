#!/bin/bash
# run this command in code directory.
[ -d "../input" ] || {
    echo "Expecting input files in code/../input directory with following structure:"
    echo "IVA/DD.MM.YYYY/NN/archive.iva"
    echo "Please provide input"
    exit
}

[ -d "../output/" ] || { 
	echo "Creating code/../output directory to write final file there"
	mkdir ../output 
}

mkdir temp
for i in `ls ../input/IVA`
do
    dir=temp/$(echo $i | awk  'BEGIN{ FS="."};{ print $3$2$1}')
    mkdir $dir
    cp -r ../input/IVA/$i/* $dir
done

cd temp
echo '' >  list.txt
for i in `ls -1 | sort`
do
    for j in `ls -1 $i | grep -v list | sort`
    do
    cp $i/$j/archive.iva $i/$j/archive.mjpeg
    echo "Wait converting file $i/$j/archive.iva"
    ffmpeg  -loglevel -8 -i $i/$j/archive.mjpeg $i/$j/archive.mp4
    echo file $i/$j/archive.mp4 >> list.txt
    done
done

echo "Merging all files to output/archive.mp4 in output directory"
echo "Be patient this may take a little longer time"


ffmpeg -loglevel -8 -f concat -i list.txt "../../output/archive.mp4"

cd ..
rm -r temp
