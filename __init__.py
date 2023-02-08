from mycroft import MycroftSkill, intent_file_handler
import nltk
from nltk.tokenize import word_tokenize


class Nltkprova(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('nltkprova.intent')
    def handle_nltkprova(self, message):
        py_txt = word_tokenize (message)
        self.speak_dialog(py_txt)


def create_skill():
    return Nltkprova()

