###
    # Code by Olzhas Kurenov
    # Implementation of Straightforward Prim's Minimum Spanning Tree Algorithm
    # (without using a Heap)
    # Running time: O(n * m)
###
print '\n~~~~~~~~~Prim\'s Minimum Spanning Tree~~~~~~~~~\n';

graph = {};
explored = [];
totalCost = 0;

f = open('edges.txt', 'r');
n, m = [int(x) for x in f.readline().split()];
for line in f.readlines():
    v, w, cost = [int(x) for x in line.split()];
    if v not in graph:
        graph[v] = {
            'explored': False,
            'edges': {}
        };
    graph[v]['edges'][w] = cost;

    if w not in graph:
        graph[w] = {
            'explored': False,
            'edges': {}
        };
    graph[w]['edges'][v] = cost;
f.close();

def minimumSpanningTree(g, s = None):
    global  explored, totalCost;
    if s >= 0:
        g[s]['explored'] = True;
        explored.append(s);
    v = None;
    w = None;
    minCost = 1000000;
    for e in explored:
        for d in g[e]['edges']:
            if d in g and not g[d]['explored']:
                cost = g[e]['edges'][d];
                if cost < minCost:
                    minCost = cost;
                    v = e;
                    w = d;
    print v, w, minCost
    if v > 0 and w > 0:
        g[w]['explored'] = True;
        explored.append(w);
        totalCost += minCost;
        minimumSpanningTree(g);

minimumSpanningTree(graph, 1);

print totalCost;
print len(explored);

# -3612829
