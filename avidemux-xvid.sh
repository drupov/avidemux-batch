#!/bin/bash

IFS=$(echo -en "\n\b")

for FIL in `ls *mp4 | sort` ; do
  yes | avidemux3_cli --load "$FIL" --run settings-xvid.py --save ${FIL%.*}.avi --quit
done