# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:09:30 2021
Library file for problem 1
@author: Evan
"""
from base64 import b64encode
import binascii

def hexToBin(inputData):


    output = bin(int(inputData, 16))

    return output


#def binToB64(inputData):
#    
#    output = 
#    
#    return output
#
#
#def binToAscii(inputData):
#    
#    output = 
#    
#    return output
#

#expects inputData as string
def hexToAscii(inputData):
    
    output = binascii.unhexlify(inputData)
    
    return output

def asciiToB64(inputData):
    
    output = b64encode(inputData)
    
    return output