import nltk
from nltk import FreqDist
from nltk.classify.naivebayes import NaiveBayesClassifier
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus.reader import CategorizedPlaintextCorpusReader


class App:

    def makeTrainingData (reader):
        for category in reader.categories():
            for file in reader.fileids(category):
                yield FreqDist(reader.words(fileids=[file])), category



    corpusDirectory = "../../resources/input/"
    #Was using PlaintextCorpusReader, switched to Categorized to provide categories
    wattsCorpus = PlaintextCorpusReader(corpusDirectory, '.*')

    print wattsCorpus.raw().strip()
    print wattsCorpus.words()
    for sentence in wattsCorpus.sents():
        print sentence
    print len(wattsCorpus.sents())
    text = nltk.tokenize.word_tokenize(wattsCorpus.raw())
    print "tokenized text: ", text

    #example of finding similar word
    text = nltk.Text(word.lower() for word in wattsCorpus.words())
    print "similar to god: ", text.similar('god')

    words = nltk.pos_tag(text)
    fdist = nltk.FreqDist(words)
    print "frequencey distribution: ", fdist

    sentence = "So there are two ways of playing the game. The first way, which is the usual way, is that a guru or teacher who wants "
    sentenceWords = nltk.word_tokenize(sentence)
    fdistForSentence = nltk.FreqDist(sentenceWords)
    fdistForSentence.plot()

    #classifier = NaiveBayesClassifier.train(list(makeTrainingData(wattsCorpus)))
