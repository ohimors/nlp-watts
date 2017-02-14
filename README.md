# nlp-watts
nlp practice with watts lectures.  The purpose of this project is to answer the following:
What categories does Watts talk about?
What are his most frequent words?
What symbols does Watts use?
Output a frequency word distribution


# [x] Output frequency word distribution
    1.  What else can we do with a frequency distribution?
# NLP Topics
    1. Frequency Distribution 
        1.  Two types *derived* and *analytic*  (probably just past/behavioral versus future/predictive)
        2.  Also includes *conditional probability distributions*
    2. K means clustering

http://deoxy.org/watts.htm

#Python console tips
    ##Encoding Problem: 
        When tokenizing the system needs a UTF8 default encoding, otherwise special characters cause the tokenizer to throw an exception.
```python
import sys
reload(sys)
sys.setdeaultencoding('UTF8')
tokens = ntlk.word_tokenize(file_content)
 ```
        
    ## Create own corpora
 ```python
    wattsCorpus = PlaintextCorpusReader('corpus/directory/path', '.*')
 ```
 
# What to do next?
I guess K means clustering sticks out to me.  I"m not sure what I'd use it for.  I think I'd like to be able to both integrate and understand new AI techniques.  I don't have a problem to solve.  I suppose I'd like to understand what Alan Watts talks about the most.  How he draws comparisons.  What symbols he uses.  Perhaps his average length of word.  Maybe I'll just start with some basic features of his language.  From reading his material I've found intersections of things he like to talk about in his speeches and books he recommends.  THere isn't anything too surprising about them other than it seems (not confirmed) that the vast majority of the stuff Watts speaks about comes from other books he read at the time of the speech.  He appears to be good at amalgamating different theories into a cohesive story.  Maybe that's all a good orator needs to do?

So it looks like I was in the middle of creating a corpus of text. 
 
For my currently example it looks like my reader needs categories so I started looking at ways to add categories.  How one gets categories seems to be a bit fuzzy.  Some example seem to pre label file categories, like separating some files into negative senitment and others into positive-- which seems to defeat the purpose.  I expect a categorizer to run through my text and output relevant categories based on frequency distribution in the text.  Perhaps this is the wrong idea.  The key problem is how do I add categories to my watt's corpus.

# Notes
    1.  find . -name "*watts*" 

# Definitions:
  Frequency Distribution - Referring to the FD of the word versus the text.  It counts observable events such as the appearance of a word in a text
  Bag of Words - a model for text used to predict sentiment.  The bag is the set of sentences but the order and grammar is disregarded while the multiplicty of a word (or frequency distribution) is salient.  
  Sequence Labeling -
  N-gram model -
  backoff -
  evaluation -
  POS tagging - Part of Speech tagging or 'POS-tagging' or simply tagging
  lexical categories - noun, verb, adverb, pronoun, adjectives
  
# Resources
    [] Read NLTK book
        - http://www.nltk.org/book/ch05.html -- good for tokenizing words
    
#definitions
    Hapax
    : A word that only appears once within a text
    Lidstone smoothing
    :
    Interpolation
    : a method of constructing new data points within the range of a discrete set of known data points