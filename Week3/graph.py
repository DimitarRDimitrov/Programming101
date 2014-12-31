class DirectedGraph():
    def __init__(self):
        self.graph = {}

    def addEdge(self, nodeA, nodeB):
        if nodeA in self.graph and nodeB in self.graph[nodeA]:
            print('The path already exists')
            return self.graph
        elif nodeA in self.graph and nodeB not in self.graph[nodeA]:
            self.graph[nodeA].append(nodeB)
            if nodeB not in self.graph:
                self.graph[nodeB] = []
            return self.graph
        else:
            self.graph[nodeA] = [nodeB]
            if nodeB not in self.graph:
                self.graph[nodeB] = []
            return self.graph

    def getNeighborsFor(self, node):
        if node in self.graph:
            return self.graph[node]
        else:
            print("The node does not exist")
            return False

    def pathBetween(self, nodeA, nodeB, path=[]):
        path = path + [nodeA]
        if nodeA == nodeB:
            return path
        if nodeA not in self.graph:
            return None
        for node in self.graph[nodeA]:
            if node not in path:
                newpath = self.pathBetween(node, nodeB, path)
                if newpath:
                    return newpath
        return None

    def toString(self):
        for node in self.graph:
            print("%s: %s" % (node, self.getNeighborsFor(node)))


my_graph = DirectedGraph()
my_graph.addEdge('A', 'B')
my_graph.addEdge('B', 'C')
my_graph.addEdge('C', 'D')
my_graph.addEdge('D', 'F')
print(my_graph.addEdge('D', 'G'))

print(my_graph.pathBetween('A', 'G'))
my_graph.toString()
