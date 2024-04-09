import math


def bits_needed(dictionary_length):
    if dictionary_length == 0:
        return 0
    return math.ceil(math.log2(dictionary_length))


def lzw_compress(input_data):
    dictionary = {chr(i): i for i in range(128)}
    dict_size = 128
    current_sequence = ""
    compress = []
    # print(dictionary)

    for symbol in input_data:
        sequence_symbol = current_sequence + symbol
        # print("--------------------------------------------")
        # print(sequence_symbol)
        if sequence_symbol in dictionary:
            current_sequence = sequence_symbol
        else:
            compress.append(dictionary[current_sequence])
            dictionary[sequence_symbol] = dict_size
            dict_size += 1
            current_sequence = symbol
        # print(compressed_data)

    if current_sequence:
        compress.append(dictionary[current_sequence])
    print(dictionary)
    if len(dictionary) > 4096:
        raise Exception("Dictionary limit exceeded")
    return compress, bits_needed(len(dictionary))


def lzw_decompress(compressed_data):
    dictionary = {i: chr(i) for i in range(128)}
    dict_size = 128

    result = current_sequence = chr(compressed_data[0])
    for code in compressed_data:
        if code in dictionary:
            entry = dictionary[code]
        elif code == dict_size:
            entry = current_sequence + current_sequence[0]
        result += entry

        dictionary[dict_size] = current_sequence + entry[0]
        dict_size += 1

        current_sequence = entry

    return result


file_path = 'a.txt'

with open(file_path, 'r') as file:
    input_data_list = list(''.join(line.strip() for line in file))

compressed_data, bits_for_encoding = lzw_compress(input_data_list)
decompressed_data = lzw_decompress(compressed_data)

print("Compressed data:", compressed_data)
print("Decompressed data:", decompressed_data)

original_size = len(input_data_list)
compressed_size = len(compressed_data)*bits_for_encoding/8
vkk = compressed_size / original_size
print("Vojšič Compression Coefficient (VKK):", vkk)
