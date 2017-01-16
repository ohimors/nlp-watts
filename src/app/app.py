from nltk import FreqDest
from nltk.classify.naivebayes import  NaiveBayesClassifier
from nltk.corpus.reader.plaintext import PlaintextCorpusReader


class App:

    def makeTrainingData (reader):
        for category in reader.categories():
            for file in reader.fileids(category):
                yield FreqDest(reader.words(fileids=[file])), category



    corpusDirectory = "../../resources/input/"
    wattsCorpus = PlaintextCorpusReader(corpusDirectory, '.*')

    print wattsCorpus.raw().strip()
    print wattsCorpus.words()
    for sentence in wattsCorpus.sents():
        print sentence
    print len(wattsCorpus.sents())

    classifier = NaiveBayesClassifier.train(list(makeTrainingData(wattsCorpus)))
