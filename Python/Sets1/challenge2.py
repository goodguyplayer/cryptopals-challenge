# -*- coding: utf-8 -*-
"""

Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965

... should produce:

746865206b696420646f6e277420706c6179

"""


def convert_hex_to_raw_byte(input_str: str):
    return bytes.fromhex(input_str)

def string_to_raw_byte(input_str: str):    
    return input_str.encode('utf-8')

# Todo - XOR with xor_key
def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


input_puzzle = "1c0111001f010100061a024b53535009181c"
xor_key = "686974207468652062756c6c277320657965"
result_puzzle = "746865206b696420646f6e277420706c6179"

# Converting both strings was necessary before the XOR

input_raw = convert_hex_to_raw_byte(input_puzzle)
key_raw = convert_hex_to_raw_byte(xor_key)
xor_result = (byte_xor(input_raw, key_raw)).hex()

if (xor_result == result_puzzle):
    print("Success")
    print(convert_hex_to_raw_byte(xor_result))
else:
    print("Failed")

