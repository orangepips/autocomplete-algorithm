import unittest
from autocomplete import *
import re, collections
import sys
import timeit

class MyTestCase(unittest.TestCase):
    def test_example_passage(self):
        acp = AutocompleteProvider()
        acp.train("The third thing that I need to tell you is that this thing does not think thoroughly.")
        self.assertCountEqual(acp.getWords("thi"), self.tuples2Candidates([("thing", 2), ("think", 1), ("third", 1), ("this", 1)]))
        self.assertCountEqual(acp.getWords("nee"), self.tuples2Candidates([("need", 1)]))
        self.assertCountEqual(acp.getWords("th"), self.tuples2Candidates([("that", 2), ("thing",2), ("think", 1),
                                              ("this", 1), ("third", 1), ("the", 1), ("thoroughly", 1)]))

    def test_big_txt(self):
        """
        big.txt and some supporting code taken from http://norvig.com/spell-correct.html
        demonstrates that the backing trie data structure used significantly reduces the size needed
        """

        big_file = open('big.txt')
        big_file_words = re.findall('[a-z]+', big_file.read().lower())
        word_counts = collections.Counter(big_file_words)

        acp = AutocompleteProvider()
        acp.train(' '.join(big_file_words))

        print("Word Count: " + str(sys.getsizeof(word_counts)) + "\t ACP: " + str(sys.getsizeof(acp)))

        self.assertGreater(sys.getsizeof(word_counts), sys.getsizeof(acp))

        print("Get Words: " + str(timeit.timeit(stmt=lambda: acp.getWords("choc"), number=1000000) / 1000000) + " secs average")


    def tuples2Candidates(self, tuples):
        candidates = []
        for tuple in tuples:
            candidates.append(Candidate(tuple[0], tuple[1]))
        return candidates

if __name__ == '__main__':
    unittest.main()
