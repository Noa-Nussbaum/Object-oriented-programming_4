# Object-oriented-programming

## Assignment 4

### Ariel University

_General Overview_

In this assignment, we were given several interfaces to implement; The Digraph and GraphAlgo interfaces. In order to implement them and to write the required functions, we had to use different data structures to match to our needs. In addition, we created various classes in order to achieve the best results and the highest efficiency levels. After completing this stage, we were instructed to build a class in which we finally presented the graphs.

_DiGraph_

In this interface, we built the graph object, implementing the Graph Interface we were given. The object parameters include a nodes dictionary and an edges dictionary, as well as a variable which counts the number of changes made to the graph since initialization.
In this class, we've created functions allowing the user to make changes to the graph, such as adding nodes and edges, getting all the edges leaving and entering a given node, and removing nodes and edges.

_GraphAlgo_

In GraphAlgo, we implemented the GraphAlgo interface. We wrote functions that run different algorithms on the Digraph object. For example, the Shortest Path function finds the shortest path existing between two given nodes. In addition, the TSP function solves the Travelling Salesman Problem in the graph. In order to implement them, we wrote the Dijkstra function as a helper.

_Tests_

The TestDiGraph and TestGraphAlgo classes run tests on both of the classes,respectively. We tested them using JSON files which hold great amounts of nodes and edges in order to check efficiency.

Here is a link to the assignment: https://docs.google.com/document/d/1LrXIX2pLvRIVHdSqVIimCCxL7UBMaogAcLKfr2dOjHk/edit
