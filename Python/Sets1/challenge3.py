# -*- coding: utf-8 -*-
"""
Single-byte XOR cipher

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. 
Character frequency is a good metric. 
Evaluate each output and choose the one with the best score. 



"You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter."
"""

def convert_hex_to_raw_byte(input_str: str):
    return bytes.fromhex(input_str)

def string_to_raw_byte(input_str: str):    
    return input_str.encode('utf-8')

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

hex_enc_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
raw_enc_str = convert_hex_to_raw_byte(hex_enc_str)

for i in range(97, 123):
    current_test = string_to_raw_byte(chr(i)*len(raw_enc_str))
    test = byte_xor(raw_enc_str, current_test).decode("utf-8") 
    print("Letter.: " + chr(i))
    print(test)
    print("-------")
    
after_run = string_to_raw_byte("x"*len(raw_enc_str))
print(byte_xor(raw_enc_str, after_run).decode("utf-8"))