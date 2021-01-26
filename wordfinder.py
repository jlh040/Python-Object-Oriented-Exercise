"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    
    def __init__(self, path):
        self.path = path
        self.list_of_words = []
        self.get_words()
        self.print_num_of_words()


    def get_words(self):
        words = open(self.path, 'r')
        for word in words:
            self.list_of_words.append(word[:-1])
        words.close()
        
    def print_num_of_words(self):
        print(f'{len(self.list_of_words)} words read')

    def random(self):
        return choice(self.list_of_words)

