#!/bin/bash

./convert_bmp.py $1

potrace -s -n -a 2 -t 0 -o ~/Desktop/out.svg -- out.bmp

rm out.bmp
