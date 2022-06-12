# -*- coding: utf-8 -*-
"""
Task 7.2b

Make a copy of the code from the task 7.2a.
Add this functionality: instead of printing to stdout,
the script should write the resulting lines to a file.

File names must be passed as arguments to the script:
  1. name of the source configuration file
  2. name of the destination configuration file

In this case, the lines that are contained in the ignore list and lines
that start with ! must be filtered.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

#ignore = ["duplex", "alias", "configuration"]
from sys import argv

 
filename = argv[1] #'config_sw1.txt'
fileDestino = argv [2]

with open(filename) as f:
    for line in f:
       #words = line.split()
      # words_intersect = set(words) & set(ignore)
       #print (words_intersect)
       if not line.startswith("!"):# and not words_intersect:
           with open(fileDestino, 'a') as a:
              a.write(line.rstrip())
