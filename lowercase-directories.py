#! /usr/local/bin/python3

import os

# make all files in the current directory into lowercase
for file in os.listdir():
    if os.path.isdir(file):
        os.rename(file, file.lower())
