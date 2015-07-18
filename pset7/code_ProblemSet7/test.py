import string

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()
        
    def isWordIn(self, text):
        text_copy = text[:]
        text_copy = text_copy.lower()
        print(text_copy)
        for char in string.punctuation:
            if char in text_copy:
                text_copy = text_copy.replace(char, ' ')
                print(text_copy)

        text_list = text_copy.split()
        print(text_list)
        return self.word in text_list

class TitleTrigger(WordTrigger):
    def evaluate(self, text):
        return self.isWordIn(text.getTitle())

class SubjectTrigger(WordTrigger):
    def evaluate(self, text):
        return self.isWordIn(text.getSubject())
        
class SummaryTrigger(WordTrigger):
    def evaluate(self, text):
        return self.isWordIn(text.getSummary())
