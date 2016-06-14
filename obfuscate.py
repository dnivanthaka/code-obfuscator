#!/usr/bin/env python3
import sys, os

filetype = ''

fpin = open(sys.argv[1], 'r')
fpout = open(sys.argv[2], 'w')

#file_name, file_extension = os.path.splitext(sys.argv[1])

for line in fpin:
    #print(file, end='')
    if ".php" in sys.argv[1] and "//" in line:
        continue
    
    if ".php" in sys.argv[1] and not ("<?php" in line) or ("?>" in line):
        writeLine = line.replace('\n', '').replace('\t', '').replace('\r', '')
    else:
        writeLine = line
    fpout.write(writeLine)
    
fpin.close();
fpout.close();
    
