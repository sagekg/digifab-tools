#!/bin/bash

./convert_bmp.py $1

potrace -s -n -a 1 -t 0 -o ~/Desktop/out.svg -- out.bmp

rm out.bmp
