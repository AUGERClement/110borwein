#!/bin/python3
# -*-coding:Utf-8 -*

import math
import methods
from os import sys

if (len(sys.argv) != 2):
    quit (84)
try:
    n = int(sys.argv[1])
except:
    if (sys.argv[1] != "-h"):
        quit(84)
    else:
        print('Pranked. There no help here !\nYou\'re alone.')
        quit(0)
h = 0.5
methods.rect(n, h)
print('')
methods.trapeze(n, h)
print('')
methods.simpson(n, h)
