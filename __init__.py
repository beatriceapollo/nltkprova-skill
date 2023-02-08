from mycroft import MycroftSkill, intent_file_handler


class Nltkprova(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('nltkprova.intent')
    def handle_nltkprova(self, message):
        self.speak_dialog('nltkprova')


def create_skill():
    return Nltkprova()

