# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 23:46:54 2021

@author: Evan
"""

#runscript

from lib import hexToAscii


import numpy as np

f = open('input.txt')

content = f.read()

byteFile = hexToAscii(content)

print(byteFile.decode('ascii'))

output = asciiToB64(byteFile).decode('ascii')

print(output)


f2 = open('outputCheck.txt')

content2 = f2.read()
print(content2)

if (output == content2):
    print('Strings are equal')
else:
    print('Strings are not equal')    