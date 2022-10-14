# 1. Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
# Determine the required attributes-data and attributes-methods in class for working with the text file.
import string
from os.path import isfile
import re

class TxtFileSP:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.__chars: list[str]
        self.__words: list[str]
        self.__sentences: list[str]
        self.__num_chars: list
        self.__num_words: int
        self.__num_sentences: int

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, name):
        if not isfile(name):
            raise FileNotFoundError

        self.__file_name = name

        with open(self.__file_name) as fl:
            # Reading raw input with all of the \n and double+ spaces
            self.__raw_text = fl.read()
            # Getting rid of \n and extra spaces
            self.__edited_text = self.__raw_text.replace("\n", " ")
            while "  " in self.__edited_text:
                self.__edited_text = self.__edited_text.replace("  ", " ")

        self.counting()

    @property
    def raw_text(self):
        return self.__raw_text

    @property
    def edited_text(self):
        return self.__edited_text

    def counting(self):
        chars = []

        # adding every character to the list
        for i in self.__raw_text.replace("\n", ""):
            chars.append(i)

        # adding every word to the list
        words = self.__edited_text.split()

        # adding sentences to the list
        sentences = re.split('\. |\! |\? ', self.__edited_text)

        self.__chars = chars
        self.__words = words
        self.__sentences = sentences
        temp = [" "]
        self.__num_chars = [len(self.__chars), len(list(filter(" ".__ne__, self.__chars)))]
        self.__num_words = len(self.__words)
        self.__num_sentences = len(self.__sentences)

    @property
    def chars(self):
        return self.__chars

    @property
    def words(self):
        return self.__words

    @property
    def sentences(self):
        return self.__sentences

    @property
    def num_chars(self):
        return self.__num_chars[0]

    # Additional function to get access to other character count without spaces
    def get_char_count(self, delete_spaces=False):
        return self.__num_chars[1] if delete_spaces else self.__num_chars[0]

    @property
    def num_words(self):
        return self.__num_words

    @property
    def num_sentences(self):
        return self.__num_sentences

    def __str__(self):
        return f'{self.__file_name}\n' \
               f'Characters in file (with/without spaces): {self.__num_chars[0]}/{self.__num_chars[1]}\n' \
               f'Words in file: {self.__num_words}\nSentences in file: {self.__num_sentences}'


my_test = TxtFileSP("Test.txt")
print(my_test)
