class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = ''.join(sorted(self.word))

    def match(self, list):
        return [word for word in list if ''.join(sorted(word.lower())) == self.sorted_word]