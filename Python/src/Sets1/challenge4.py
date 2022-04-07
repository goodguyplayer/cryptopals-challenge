"""

Detect single-character XOR
One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)

"""

from Python.src.functions.import_functions import load_file

def convert_hex_to_raw_byte(input_str: str):
    return bytes.fromhex(input_str)

def string_to_raw_byte(input_str: str):
    return input_str.encode('utf-8')

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])




if __name__ == '__main__':
    file_input = load_file("challenge4.txt")
    for line in file_input:
        raw_enc_str = string_to_raw_byte(line)
        for i in range(97, 123):
            current_test = string_to_raw_byte(chr(i) * len(raw_enc_str))
            test = byte_xor(raw_enc_str, current_test).decode("utf-8")
        after_run = string_to_raw_byte("x" * len(raw_enc_str))
        print(byte_xor(raw_enc_str, after_run).decode("utf-8"))