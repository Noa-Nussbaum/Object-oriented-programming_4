from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
from GraphAlgo import GraphAlgo
from pygame import *

WIDTH, HEIGHT = 1080, 720
PORT = 6666
HOST = '127.0.0.1'
pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

client = Client()
client.start_connection(HOST, PORT)

file = client.get_graph()

# graph = json.loads(
#     file, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

g = GraphAlgo()
g.load_from_json(file)
print(g)

pokemons = client.get_pokemons()
poke = g.load_pokemons(pokemons)

print(poke)