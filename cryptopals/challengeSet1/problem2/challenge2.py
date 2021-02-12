# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 00:13:36 2021

@author: Evan
"""
import binascii

str1 = '1c0111001f010100061a024b53535009181c'

str2 = '686974207468652062756c6c277320657965'

outputTestStr = '746865206b696420646f6e277420706c6179'

str1B = bytes.fromhex(str1)

str2B = bytes.fromhex(str2)


xOutput = b''

for b1,b2 in zip(str1B,str2B):
    xOutput += bytes([b1^b2])


print(xOutput)
print(str1B)
print(str2B)

output = binascii.hexlify(xOutput).decode('ascii')

if (output == outputTestStr):
    print('Strings are equal')
else:
    print('Strings are not equal')    