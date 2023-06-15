class TextSwap:
    @staticmethod
    def swap(sentence, code_array):
        return ''.join(code_array.get(c, c) for c in sentence)
