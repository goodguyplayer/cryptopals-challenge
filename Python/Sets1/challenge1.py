# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:00:41 2022

@author: Nathan
"""

# https://cryptopals.com/sets/1/challenges/1

"""
Convert hex to base64

The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

Rule.: Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing. 
"""

import base64

def convert_hex_to_raw_byte(input_str: str):
    return bytes.fromhex(input_str)

input_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
result_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

temp = (convert_hex_to_raw_byte(input_str))
temp = base64.b64encode(temp).decode()

if (temp == result_str):
    print("Success")
    print(temp)
else:
    print("Failed")