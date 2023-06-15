class HuffmanDecoder:
    @staticmethod
    def decode(coded_sentence, roots):
        decoded_sequence = []
        node = roots

        for bit in coded_sentence:
            if bit == '0':
                node = node.left_child
            elif bit == '1':
                node = node.right_child

            if not node.left_child and not node.right_child:
                decoded_sequence.append(node.key)
                node = roots

        return ''.join(decoded_sequence)