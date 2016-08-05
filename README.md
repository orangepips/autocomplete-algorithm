# autocomplete-algorithm

Solution for "Mobile Device Keyboard" from http://asymmetrik.com/programming-challenges/

Uses https://github.com/pytries/datrie 

Built with Python 3.5.2 

See [autocomplete.py](autocomplete.py)
 
# Commentary 

The key to the problem is the final clue _The third thing that I need to tell you is that this thing does not think thoroughly._
 
This can be taken to mean that spelling corrections are not a requirement, greatly simplifying the problem. 

Otherwise it would be a matter of pursuing a solution using a Directed Acyclic Word Graph (DAWG) ordered by frequency as described in https://www.strchr.com/dawg_predictive. Unfortunately that appproach does not appear to offer a way to update in an online fashion. So a potentially even more sophisticated solution is presented in the research paper referenced here http://www.rene-pickhardt.de/the-best-way-to-create-an-autocomplete-service-and-the-winner-is-giuseppe-ottaviano/

# Problem Description

We are developing a keyboard autocomplete algorithm to be used in various mobile devices. This algorithm will analyze the passages typed by the user in order to suggest a set of candidate autocomplete words given a word fragment.

We need you to write the algorithm that will learn the words typed by the user over time and then determine a ranked list of autocomplete candidates given a word fragment (you should ignore capitalization when providing suggestions). The algorithm will be trained in an online manner, meaning that additional training passages can be submitted and incorporated into the algorithm at the same time as the algorithm is being used to provide autocomplete suggestions. Ideally, the accuracy of the algorithm will improve over time as more and more training passages are incorporated. Due to the deployment environment for this algorithm, efficiency is critical. The data structure utilized by your algorithm should be optimized for space and time. We have provided a specification [1] and a sample passage [2] along with example input and output and would like you to provide the implementation.

## [1] INTERFACE SPECIFICATION

```
Candidate
    String getWord() : returns the autocomplete candidate
    Integer getConfidence() : returns the confidence* for the candidate

AutocompleteProvider
    List<Candidate> getWords(String fragment) : returns list of candidates ordered by confidence*
    void train(String passage) : trains the algorithm with the provided passage
```

* Confidence is the likelihood/relevance of an individual word relative to the other words being returned by the autocomplete provider. If two words are equally likely, they should have the same confidence. If one is more likely, it should have a higher confidence.

## [2] EXAMPLE WORDS AND THEIR EXPECTED NEXT WORDS BASED ON THE PROVIDED PASSAGES

```
Train: "The third thing that I need to tell you is that this thing does not think thoroughly."
Input: "thi" --> "thing" (2), "think" (1), "third" (1), "this" (1)
Input: "nee" --> "need" (1)
Input: "th" --> "that" (2), "thing" (2), "think" (1), "this" (1), "third" (1), "the" (1), "thoroughly" (1)
```

# Other Research
 
http://suggesttree.sourceforge.net/ 