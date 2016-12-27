# nlp-watts
nlp practice with watts lectures.  The purpose of this project is to answer the following:
What categories does Watts talk about?
What are his most frequent words?
What symbols does Watts use?
Output a frequency word distribution


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