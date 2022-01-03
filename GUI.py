from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
from Node import Node
from GraphAlgo import GraphAlgo
from pygame import *

WIDTH, HEIGHT = 1080, 720
PORT = 6666
HOST = '127.0.0.1'

pygame.init()

client = Client()
client.start_connection(HOST, PORT)

# Get the graph
file = client.get_graph()
graph = GraphAlgo()
graph.load_from_json(file)
print(graph)

# Get the pokemons
pokemon_list = client.get_pokemons()
pokemons = graph.load_pokemons(pokemon_list)
print(pokemons)

# Get the agents
info = json.loads(client.get_info())
num_agents = info['GameServer']['agents']
for n in range(num_agents):
    name = "{\"id\":"+str(n)+"}"
    client.add_agent(name)

agent_list = client.get_agents()
agents = graph.load_agents(agent_list)
print(agents)

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
pygame.display.set_caption("Pokemon Game - Ex4")

pygame.font.init()
FONT = pygame.font.SysFont('Arial', 20, bold=True)
clock = pygame.time.Clock()

client.start()

while client.is_running() == 'true':
    # Draw the graph

    # Get the nodes
    for n,node in graph.nodes.items():
        pygame.draw.circle(screen, (0, 0, 255), [node.getPos()[0], node.getPos()[1]], 5)

    # draw the node id
    id_srf = FONT.render(str(node.getId()), True, Color(255, 255, 255))
    rect = id_srf.get_rect(center=(node.getPos()[0], node.getPos()[1]))
    screen.blit(id_srf, rect)


    # Get pokemons
    # Get agents

    # Color the screen
    screen.fill(Color(0, 0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)



