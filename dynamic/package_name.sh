#!/bin/bash
aapt dump badging $1 | grep package | sed -r "s/package: name='([a-z0-9.]*)'.*/\1/" > /home/venkatesh/fyp/github/final_year_project/dynamic/package_name.txt