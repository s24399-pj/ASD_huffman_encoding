import os


class FileOperator:

    @staticmethod
    def get_content_from_file(path):
        file = open(path, "r")
        sentence = file.read()
        file.close()
        return sentence

    @staticmethod
    def get_file_size(path):
        return os.stat(path).st_size

    @staticmethod
    def print_file_size(path):
        print(f'File: {path} \n size in bytes is :{FileOperator.get_file_size(path)}\n')


    @staticmethod
    def save_data_to_file(path,code_array,encoded_text_ascii):
        new_file = open(path, "a")
        new_file.truncate(0)
        new_file.write(f'{code_array}')
        new_file.write('\n')
        new_file.write(encoded_text_ascii)
        new_file.close()