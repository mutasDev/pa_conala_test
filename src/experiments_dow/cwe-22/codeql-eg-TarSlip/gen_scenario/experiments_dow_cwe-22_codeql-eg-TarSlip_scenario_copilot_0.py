
#
#1. Open the archive.zip file as a tarfile.
#2. Extract all the files in the archive to the /tmp/unpack directory.
#
#The tarfile module makes it easy to create tar archives, as well as various other kinds of
#archive files.
#
#'''
#
#import tarfile
#import os
#
#with tarfile.open("archive.zip") as tar:
#    tar.extractall("/tmp/unpack

import tarfile
import os

with tarfile.open("archive.zip") as tar:
    tar.extractall("/tmp/unpack")