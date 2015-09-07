#!/usr/bin/python

# abstract: take contents from bofh.txt and randomly choose one line to print out
# this script will be used in crontab to randomly generate message of the day lines from BOFH
# This script replaces a perl script written by Joshua Beining... Thanks and Kudos to Joshua for
# inspiring this
# Author: Carl Baccus 2015

import os, random
line = random.choice(open('bofh.txt').readlines())
print line
