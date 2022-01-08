from typing import List
import json
from numpy import double
from DiGraph import DiGraph
import random
from PokemonUtils import Pokemon
from AgentUtils import Agent
import matplotlib.pyplot as plt

class GraphAlgo():

    def __init__(self)-> None:
        self.nodes = {}
        self.edges = {}
        self.graph = DiGraph()

    def __repr__(self):
        return f"Nodes: {self.nodes}\nEdges: {self.edges}\n"

    def get_graph(self):
        return self.graph

    def load_from_json(self, info: str):
        self.__init__()
        graph = DiGraph()
        dict = json.loads(info)
        for n in range(len(dict["Nodes"])):
            id = dict["Nodes"][n]["id"]
            pos = dict["Nodes"][n]["pos"]
            tuple = pos.split(',')
            graph.add_node(id, tuple)
        for e in range(len(dict["Edges"])):
            src = dict["Edges"][e]["src"]
            dest = dict["Edges"][e]["dest"]
            w = dict["Edges"][e]["w"]
            graph.add_edge(src,dest,w)
        self.edges=graph.edges
        self.nodes=graph.nodes
        self.graph=graph


    def dijkstra(self, src: int) -> (list, list):
        unvisited = list(self.nodes.keys())

        shortest_from_src = {i: float('inf') for i in unvisited}  # dist between src and other nodes
        shortest_from_src[src] = 0  # dist from src to itself is 0

        previous_nodes = {}

        while unvisited:
            current = None
            # let's find the node with the lowest weight value
            for node in unvisited:
                if current == None:
                    current = node
                elif shortest_from_src[node] < shortest_from_src[current]:
                    current = node

            neighbors = self.graph.all_out_edges_of_node(current)

            for i in range(len(neighbors)):
                m = list(neighbors[i])
                value = shortest_from_src[current] + neighbors[i].get(m[0])
                if value < shortest_from_src[m[0]]:
                    shortest_from_src[m[0]] = value
                    previous_nodes[m[0]] = current

            unvisited.remove(current)

        return previous_nodes, shortest_from_src

    def is_connected(self):
        return float('inf') not in self.dijkstra(0)[1]

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        list = self.dijkstra(id1)

        # if there is no path, return
        if list[1].get(id2) == float('inf'):
            return float('inf'), []

        answer = []
        node = id2

        while node != id1:
            answer.append(node)
            node = list[0].get(node)

        answer.append(id1)
        result = answer[::-1]

        return list[1][id2], result

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if not self.is_connected():
            return [], 0.0

        copy_cities = [j for j in node_lst] #copy node list
        result = []
        answer = 0

        temp = node_lst[0]
        result.append(copy_cities[0])
        copy_cities.remove(copy_cities[0])

        while len(copy_cities)>=1:
            min = double('inf')
            same = -1
            place = -1
            for i in range(len(copy_cities)):
                open = copy_cities[i]
                dist = (self.shortest_path(temp, open))[0]
                if dist < min:
                    min = dist
                    same = open
                    place = i
            list = self.shortest_path(temp,same)[1]
            while len(list)>=1:
                if list[0] not in result:
                    result.append(list[0])
                list.remove(list[0])
            q = copy_cities[place]
            temp=q
            copy_cities.remove(copy_cities[place])
            if len(copy_cities)==1 and same+1 not in result:
                result.append(same+1)
            for i in self.graph.edges.values():
                answer = answer + i['w']

        return result, answer



    def load_pokemons(self,pokemon_list:str) -> dict:
        pokemons = {}
        dict = json.loads(pokemon_list)
        for n in range(len(dict["Pokemons"])):
            value = dict["Pokemons"][n]["Pokemon"]["value"]
            type = dict["Pokemons"][n]["Pokemon"]["type"]
            pos = dict["Pokemons"][n]["Pokemon"]["pos"]
            p = Pokemon(value, type, pos, self.graph)
            pokemons[n]= p
        return pokemons


    def load_agents(self,agent_list:str) -> dict:
        agents = {}
        dict = json.loads(agent_list)
        for n in range(len(dict["Agents"])):
            id = dict["Agents"][n]["Agent"]["id"]
            value = dict["Agents"][n]["Agent"]["value"]
            src = dict["Agents"][n]["Agent"]["src"]
            dest = dict["Agents"][n]["Agent"]["dest"]
            speed = dict["Agents"][n]["Agent"]["speed"]
            pos = dict["Agents"][n]["Agent"]["pos"]
            agent = Agent(id,value,src,dest,speed,pos)
            agents[n]= agent
        return agents

    # Finds pokemon to which to send the agent
    def choosePokForAgent(self, agent: Agent,pokemons:dict):
        minDist = float('inf')
        pokemonMin = None
        index=None
        next_node=None
        for p, pokemon in pokemons.items():
            dist, next_node_temp = self.shortest_path(agent.get_src(), pokemon.get_dest())
            if dist < minDist:
                minDist = dist
                pokemonMin = pokemon
                index = p
                if len(next_node_temp)==1:
                    next_node=next_node_temp[0]
                else:
                    next_node = next_node_temp[1]
        del pokemons[index]
        return pokemonMin, next_node








