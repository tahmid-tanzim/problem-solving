#!/bin/bash

declare -a arr=(
#"http://srv5.cinehub24.com/2021/02/257657-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E01-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
#"http://srv5.cinehub24.com/2021/02/257659-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E02-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
#"http://srv5.cinehub24.com/2021/02/257658-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E03-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
#"http://srv5.cinehub24.com/2021/02/257661-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E04-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
#"http://srv5.cinehub24.com/2021/02/257660-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E05-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
#"http://srv5.cinehub24.com/2021/02/257656-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E06-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
#"http://srv5.cinehub24.com/2021/02/257662-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E07-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
#"http://srv5.cinehub24.com/2021/02/257663-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E08-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
#"http://srv5.cinehub24.com/2021/02/257665-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E09-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"
#"http://srv5.cinehub24.com/2021/02/257666-156787-Scam-1992-the-Harshad-Mehta-Story-S01-E10-WebRip-720p-Hindi-AAC-x264---mkvCinemas.mkv"

#"http://srv1.cinehub24.com/05%2F89910-61430-The-Wolf-of-Wall-Street-%282013%29--1080p-5.1CH-x264-Ganool.part1.rar"
#"http://srv1.cinehub24.com/05%2F89916-61430-The-Wolf-of-Wall-Street-%282013%29--1080p-5.1CH-x264-Ganool.part2.rar"

#"http://srv1.cinehub24.com/09%2F2142-27218-The-Godfather-I-%5B1972%5D-BRRip-H264-AAC.mp4"

#"http://srv1.cinehub24.com/10%2F37010-42829-Blood-Diamond-2006.mkv"
#"http://srv1.cinehub24.com/10%2F37011-42829-Blood-Diamond-2006.srt"

#"http://srv5.cinehub24.com/05/219800-120303-Chernobyl.S01E01.1.23.45.1080p.AMZN.WEBRip.AAC.5.1.x265-ALiEN.mkv"
#"http://srv5.cinehub24.com/05/219801-120303-Chernobyl.S01E02.Please.Remain.Calm.1080p.AMZN.WEBRip.AAC.5.1.x265-ALiEN.mkv"
#"http://srv5.cinehub24.com/05/219890-120303-Chernobyl.S01E03.Open.Wide.O.Earth.1080p.AMZN.WEBRip.AAC.5.1.x265-ALiEN.mkv"
#"http://srv5.cinehub24.com/05/220010-120303-Chernobyl.S01E04.The.Happiness.of.All.Mankind.1080p.AMZN.WEBRip.AAC.5.1.x265-ALiEN.mkv"
#"http://srv5.cinehub24.com/06/220637-120303-Chernobyl.S01E05.Vichnaya.Pamyat.1080p.AMZN.WEBRip.AAC.5.1.x265-ALiEN.mkv"

#"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/3.%20Required%20Setup%20for%20Programming.zip"
#"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/4.%20Introduction.zip"
#"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/5.%20Recursion.zip"
#"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/6.%20Arrays%20Representations.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/7.%20Array%20ADT.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/8.%20Strings.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/9.%20Matrices.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/10.%20Sparse%20Matrix%20and%20Polynomial%20Representation.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/11.%20Linked%20List.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/12.%20Sparse%20Matrix%20and%20Polynomial%20using%20Linked%20List.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/13.%20Stack.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/14.%20Queues.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/15.%20Trees.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/16.%20Binary%20Search%20Trees.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/17.%20AVL%20Trees.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/18.%20Search%20Trees.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/19.%20Heap.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/20.%20Sorting%20Techniques.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/21.%20Hashing%20Technique.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/22.%20Graphs.zip"
"http://192.168.1.8:8080/Udemy%20-%20Mastering%20Data%20Structures%20%26%20Algorithms%20using%20C%20and%20C%2B%2B/23.%20Asymptotic%20Notations.zip"
)

cd /Volumes/Tanzim\ 1TB\ HDD/Developer/
mkdir "Chernobyl"
cd "Udemy - Mastering Data Structures & Algorithms using C and C++"
ls -la
pwd

for i in "${arr[@]}"
do
   echo "Start Downloading ... $i"
   curl -O $i
done

echo "Download Completed..."