#!/bin/bash

IFS=$(echo -en "\n\b")

if [ -z "$1" ]; then
  echo "No argument supplied"
  exit 1
fi

if [[ "$1" != "xvid" && "$1" != "x264" ]]; then
  echo "You must pass the codec as an argument to the script, e.g. either 'xvid' ot 'x264'"
  exit 128
fi

mkdir -p dest-$1

for FIL in `ls *mp4 | sort` ; do
  yes | avidemux3_cli --load "$FIL" --run settings-$1.py --save dest-$1/${FIL%.*}.avi --quit
done
