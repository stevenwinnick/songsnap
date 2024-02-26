#!/bin/bash
# This script is used to run the audioScraper.py script

if [ $# -lt 1 ] || [ $# -gt 2 ]; then
    echo "Usage: ./try.sh <folderName> <exists>"
    echo "This will create that folder, wiping it first if <exists>"
    exit 1
fi

if [[ $2 == "0" ]]; then
    echo "Removing existing /mnt/disks/disk1/audio/$1"
    rm -r /mnt/disks/disk1/audio/$1
fi

mkdir /mnt/disks/disk1/audio/$1
python3 scraper.py songList.csv /mnt/disks/disk1/audio/$1 > /mnt/disks/disk1/audio/$1/pyLog.txt &
echo "Scraper is executing. To see number of files, do the following:"
echo "ls /mnt/disks/disk1/audio/$1 | wc -l"
exit 0