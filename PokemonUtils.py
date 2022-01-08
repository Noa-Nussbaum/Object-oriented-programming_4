import math
import DiGraph
from src.AgentUtils import Agent

class Pokemon:

    def __init__(self, value, type, pos, graph: DiGraph):
        self.value = value
        self.type = type
        self.pos = pos
        self.graph = graph
        final_src = None
        final_dest = None
        for src in graph.nodes.keys():
            srcNode = graph.nodes[src]
            for dest in graph.all_out_edges_of_node(src).items():
                dest_num = list(dest[1].keys())[0]
                destNode = graph.nodes[dest_num]
                if (type > 0 and src < dest_num) or (type < 0 and src > dest_num):
                    positions = pos.split(',')
                    srcOne = [float(srcNode.getPos()[0]), float(srcNode.getPos()[1])]
                    destTwo = [float(destNode.getPos()[0]), float(destNode.getPos()[1])]
                    lineOne = math.dist(srcOne, destTwo)
                    lineTwo = math.dist(srcOne, [float(positions[0]),float(positions[1])]) + math.dist([float(positions[0]),float(positions[1])], destTwo)
                    if lineTwo - 0.0000001 <= lineOne <= lineTwo + 0.0000001:
                        final_src = src
                        final_dest = dest_num
                        break
            if final_src is not None:
                break
        self.src = final_src
        self.dest = final_dest

    def __repr__(self) -> str:
        return "{{'Pokemon': value:{} type:{} pos:{}}}" \
            .format(self.value, self.type, self.pos)

    def get_value(self):
        return self.value

    def get_pos(self):
        return self.pos

    def get_type(self):
        return self.type

    def distance(self, src, dest):
        src = [float(src[0]),float(src[1])]
        dest = [float(dest[0]),float(dest[1])]
        return math.dist(src, dest)

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest
