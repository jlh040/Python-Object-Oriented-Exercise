from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """Make a subclass of WordFinder."""

    def __init__(self, path):
        """Get all of the attributes from WordFinder and put it on the instance."""

        super().__init__(path)

    def __repr__(self):
        """Create a string representation of the instance"""
        
        return f'SpecialWordFinder(path = \'{self.path}\')'
    
    def get_words(self):
        """Get the words from the file and check for empty lines and octothorp
        symbols.
        """

        words = open(self.path, 'r')
        for word in words:
            if word != '\n' and word[0] != '#':
                self.list_of_words.append(word[:-1])
        words.close()