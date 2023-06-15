from node import Node
from tree import Tree
from heap_node import HeapNode
from code_builder import CodeBuilder
from text_swap import TextSwap
from huffman_decoder import HuffmanDecoder


class HuffmanEncoder:
    @staticmethod
    def create_tree(sentence):
        letter_count = HuffmanEncoder.__get_letter_count(sentence)
        nodes = []

        for letter, count in letter_count.items():
            node = Node(letter, count, None, None)
            nodes.append(node)

        array_of_nodes = HeapNode.build_min_heap(nodes)
        return Tree(array_of_nodes)

    @staticmethod
    def create_code_array(tree):
        code_array = {}
        CodeBuilder.create_code_array(code_array, tree.roots, "")
        return code_array

    @staticmethod
    def encode_text(sentence, code_array):
        return TextSwap.swap(sentence, code_array)

    @staticmethod
    def decode_text(encoded_text, tree):
        return HuffmanDecoder.decode(encoded_text, tree.roots)

    @staticmethod
    def __get_letter_count(text):
        letter_count = {}
        for letter in text:
            letter_count[letter] = letter_count.get(letter, 0) + 1
        return letter_count

    @staticmethod
    def process_text(sentence):
        tree = HuffmanEncoder.create_tree(sentence)
        code_array = HuffmanEncoder.create_code_array(tree)
        encoded_text = HuffmanEncoder.encode_text(sentence, code_array)
        decoded_text = HuffmanEncoder.decode_text(encoded_text, tree)

        return encoded_text, decoded_text, code_array