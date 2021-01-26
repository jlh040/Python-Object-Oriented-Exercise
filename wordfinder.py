from random import choice


class WordFinder:
    """Finds random words from a list of words."""

    def __init__(self, path):
        """Put the list of words as an attribute on the instance, and also print out
        the number of words that were read in.
        """

        self.path = path
        self.list_of_words = []
        self.get_words()
        self.print_num_of_words()

    def get_words(self):
        """Read the file, line by line, and add each word to the list of words."""

        words = open(self.path, 'r')
        for word in words:
            self.list_of_words.append(word[:-1])
        words.close()
        
    def print_num_of_words(self):
        """Print the number of words that were read in from the file."""

        print(f'{len(self.list_of_words)} words read')

    def random(self):
        """Return a random word from the list of words."""
        return choice(self.list_of_words)

