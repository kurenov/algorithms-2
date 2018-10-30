###
    # Code by Olzhas Kurenov
    # Implementation of Straightforward Prim's Minimum Spanning Tree Algorithm
    # (without using a Heap)
    # Running time: O(n * m)
    # Answer: -3612829
###
print '\n~~~~~~~~~Prim\'s Minimum Spanning Tree~~~~~~~~~\n';

graph = {}
explored = []
totalCost = 0

def minimumSpanningTree(s = None):
    global  graph, explored, totalCost;
    if s >= 0:
        explored.append(s)
        graph[s]['explored'] = True
    minCost = 10000000
    w = None
    for e in explored:
        for d in graph[e]['edges']:
            if not graph[d]['explored']:
                cost = graph[d]['edges'][e]
                if cost < minCost:
                    minCost = cost
                    w = d
    if w > 0:
        # print w, minCost
        graph[w]['explored'] = True
        explored.append(w)
        totalCost += minCost
        minimumSpanningTree()


f = open('edges.txt', 'r')
n, m = [int(x) for  x in f.readline().split()]

for line in f.readlines():
    v, w, cost = [int(x) for x in line.split()]
    if v not in graph:
        graph[v] = {
            'explored': False,
            'edges': {}
        }
    graph[v]['edges'][w] = cost

    if w not in graph:
        graph[w] = {
            'explored': False,
            'edges': {}
        }
    graph[w]['edges'][v] = cost

# print graph
minimumSpanningTree(1)
print totalCost
