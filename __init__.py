from mycroft import MycroftSkill, intent_file_handler
import nltk
from nltk.tokenize import word_tokenize


class Nltkprova(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('nltkprova.intent')
    def handle_nltkprova(self, message):
        text = message.data.get('utterance')
        tokenized_text = word_tokenize (text)
        self.speak(print(nltk.pos_tag(tokenized_text)))


def create_skill():
    return Nltkprova()

