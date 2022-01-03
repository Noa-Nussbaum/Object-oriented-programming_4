
class Agent:

    def __init__(self,id, value, source, dest, speed,pos):
        self.id = id
        self.value = value
        self.source = source
        self.dest = dest
        self.speed = speed
        self.pos = pos

    def __repr__(self) -> str:
        return f"{'Agent': \n id:{self.value} value:{self.type} src:{self.pos} dest:{self.pos} speed:{self.pos} pos:{self.pos}}"

    def get_id(self):
        return self.id

    def get_value(self):
        return self.value

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_speed(self):
        return self.speed

    def get_pos(self):
        return self.pos

