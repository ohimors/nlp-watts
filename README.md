# nlp-watts
nlp practice with watts lectures


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