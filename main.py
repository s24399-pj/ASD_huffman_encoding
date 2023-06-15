from huffman_encoder import HuffmanEncoder
from bit_converter import BitStringConverter
from file_operator import FileOperator

file_name = "rosetta_stoned_decoded.txt"
new_file_name = "rosetta_stoned_encoded.txt"

sentence = FileOperator.get_content_from_file(file_name)

FileOperator.print_file_size(file_name)

encoded_text, decoded_text, code_array = HuffmanEncoder.process_text(sentence)
encoded_text_ascii = BitStringConverter.generate(encoded_text)

print("Encoded Text:")
print(encoded_text)
print("\n\n\n\n")
# print("\n\n\n\n")
# print("\nDecoded Text:")
# print(decoded_text)
# print("\n\n\n\n")
# print("\n\n\n\n")

FileOperator.save_data_to_file(new_file_name, code_array, encoded_text_ascii)

FileOperator.print_file_size(new_file_name)
