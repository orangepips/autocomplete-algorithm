import string
import datrie
import operator

class CommonEqualityMixin(object):
    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality test"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(tuple(sorted(self.__dict__.items())))

class Candidate(CommonEqualityMixin):
    word = None
    confidence = None

    def __init__(self, word, confidence):
        self.word = word
        self.confidence = confidence

    def getWord(self):
        """
        :return the autocomplete candidate
        """
        return self.word

    def getConfidence(self):
        """
        :return the confidence* for the candidate
        """
        return self.confidence

    def __str__(self):
        """
        :return: candidate data in the format "<word>" (<confidence>)
        """
        return '"' + self.word + '" (' + str(self.confidence) + ')' #


class AutocompleteProvider():
    # class variables
    trie_characters = string.ascii_lowercase

    def __init__(self):
        self.trie = datrie.Trie(self.trie_characters)

    def getWords(self, fragment):
        """
        :param fragment: string to lookup
        :return list of candidates ordered by confidence*
        """
        items = self.trie.items(fragment)
        items.sort(key=operator.itemgetter(1), reverse=True)

        candidates = []
        for item in items:
            candidates.append(Candidate(item[0], item[1]))
        return candidates

    def train(self, passage):
        """
        trains the algorithm with the provided passage
        :param passage: string to train autocomplete upon
        :return: nothing
        """
        words = passage.lower().split()
        for word in words:
            word = self.scrub(word)
            self.trie.setdefault(word, 0)
            self.trie[word] += 1

    def scrub(self, value):
        return ''.join(s for s in value.lower() if s in self.trie_characters)

    @staticmethod
    def words2String(words):
        return ', '.join(map(str, words))

autocompleteProvider = AutocompleteProvider()

def trainPassage(passage):
    print("Train: \"" + passage + "\"")
    autocompleteProvider.train(passage)

def printWords(word):
    words = autocompleteProvider.getWords(word)
    print("Input: \""+ word + "\" --> " + AutocompleteProvider.words2String(words))

def main():
    trainPassage("The third thing that I need to tell you is that this thing does not think thoroughly.")
    printWords("thi")
    printWords("nee")
    printWords("th")

if __name__ == "__main__":
    main()