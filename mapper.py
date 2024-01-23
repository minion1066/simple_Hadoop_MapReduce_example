#!/usr/bin/env python

# Regis University 24 Spring 8w1 MSDS 610/S40
# Emily Carpenter, Week 2, Assignment 2, Jan 22-28, 2024

import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words; splits on any whitespace
    words = line.split()

    # added for week 2 assignment
    stops = set([
        'the', 'and', 'to', 'of', 'a', 'in', 'is', 'it', 
        '.', ',', ':', ';', '-', '\'', '\"', '?', '!'
        ])

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stops:
            print '%s\t%s' % (word, "1")
