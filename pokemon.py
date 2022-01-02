
class pokemon:

    def __init__(self, value, type, pos):
        self.value = value
        self.type = type
        self.pos = pos

    def __repr__(self) -> str:
        return f"{'Pokemon': \n value:{self.value} type:{self.type} pos:{self.pos}}"

    def get_value(self):
        return self.value

    def get_pos(self):
        return self.pos

    def get_type(self):
        return self.type