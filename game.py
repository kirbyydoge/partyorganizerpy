class Game:
    emote = {}
    def __init__(self, name, emote, role):
        self.name = name.lower()
        self.emote = emote
        self.role = role

    def __gt__(self, other):
        return self.name > other.name