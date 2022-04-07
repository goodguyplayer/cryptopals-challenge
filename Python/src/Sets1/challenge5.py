"""
Implement repeating-key XOR
Here is the opening stanza of an important work of the English language:

Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

It should come out to:

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.
"""

from Python.src.functions.conversion_data import byte_xor, string_to_raw_byte


if __name__ == '__main__':
    input_string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    inp_str_byte = string_to_raw_byte(input_string)
    key_string = "ICE"
    key_string_byte = string_to_raw_byte(key_string)
    key_string_size = key_string_byte*(len(input_string)//len(key_string_byte) + 1)

    print(bytes.)




