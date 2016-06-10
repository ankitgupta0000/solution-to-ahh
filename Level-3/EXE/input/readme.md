Created input file exe.mp4 by opening "Brixton A - 91189 - cctv298204 - 00010100_1.exe" in hex editor and deleting any bit before offset 
4083924 or 0x3e50d4.  After that file is able to run on VLC media player with .h263 codec but having all videos in random order. 
Tried to analyse the file and found \xFF 99 times many places. Through which I split the file and tried to write it in 17 different files as visible on executable but it is still not splitted properly.
