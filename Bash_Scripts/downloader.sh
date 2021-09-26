#!/bin/bash

declare -a arr=(
"http://srv5.cinehub24.com/2021/02/257657-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E01-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
"http://srv5.cinehub24.com/2021/02/257659-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E02-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
"http://srv5.cinehub24.com/2021/02/257658-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E03-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
"http://srv5.cinehub24.com/2021/02/257661-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E04-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
"http://srv5.cinehub24.com/2021/02/257660-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E05-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
"http://srv5.cinehub24.com/2021/02/257656-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E06-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
"http://srv5.cinehub24.com/2021/02/257662-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E07-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
"http://srv5.cinehub24.com/2021/02/257663-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E08-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
"http://srv5.cinehub24.com/2021/02/257665-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E09-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
"http://srv5.cinehub24.com/2021/02/257666-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E10-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
)

cd /Volumes/Tanzim\ 1TB\ HDD/Movies/Scam\ 1992
ls -la
pwd

for i in "${arr[@]}"
do
   echo "Start Downloading ... $i"
   curl -O $i
done

echo "Download Completed..."