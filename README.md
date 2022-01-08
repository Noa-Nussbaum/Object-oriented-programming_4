# Object-oriented-programming

## Assignment 4

### Ariel University

_General Overview_

In this assignment, we were expected to design a “Pokemon game” in which given a weighted graph,  a set of “Agents” should be located on it so they could “catch” as many “Pokemons” as possible. The pokemons are located on the graph’s (directed) edges, therefore, the agent needs to take the proper edge to “grab” the pokemon. Our goal was to maximize the overall sum of weights of the “grabbed” pokemons (while not exceeding the maximum amount of server calls allowed in a second - 10 max). In order to achieve this, we some of the classes we created in our previous graph related assignment. In addition, we created a pokemon and an agent class. We also created a GUI class, in which we used pygame for graphics.

_DiGraph_

In this interface, we built the graph object, implementing the Graph Interface we were given. The object parameters include a nodes dictionary and an edges dictionary, as well as a variable which counts the number of changes made to the graph since initialization.
In this class, we've created functions allowing the user to make changes to the graph, such as adding nodes and edges, getting all the edges leaving and entering a given node, and removing nodes and edges.

_GraphAlgo_

In GraphAlgo, we implemented the GraphAlgo interface. We wrote functions that run different algorithms on the Digraph object. For example, the Shortest Path function finds the shortest path existing between two given nodes. In addition, the TSP function solves the Travelling Salesman Problem in the graph. In order to implement them, we wrote the Dijkstra function as a helper. For this assignment, we added two load functions, which allowed us to read and create agents and pokemons by reading them from a given JSON file.

_Tests_

The Tests class runs tests on both of the classes respectively. We tested them using JSON files which hold great amounts of nodes and edges in order to check efficiency.

[Here is a link to the assignment in GitHub](https://docs.google.com/document/d/1LrXIX2pLvRIVHdSqVIimCCxL7UBMaogAcLKfr2dOjHk/edit)
