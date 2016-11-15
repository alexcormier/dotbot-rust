import dotbot

class Rust(dotbot.Plugin):
    def can_handle(self, directive):
        return False

    def handle(self, directive, data):
        return False