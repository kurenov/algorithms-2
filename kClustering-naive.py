###
    # Code by Olzhas Kurenov
    # Implementation of a Greedy k-Clustering Algorithm
    # Running time: O(n + m)
###
import time;
print '\n~~~~~~~~~Greedy k-Clustering Algorithm~~~~~~~~~\n';

start = time.time()

graph = {};
totalClusters = 0;
targetClusters = 4;

f = open('clustering1.txt', 'r');
n = int(f.readline());
for line in f.readlines():
    v, w, distance = [int(x) for x in line.split()];
    if v not in graph:
        graph[v] = {
            'cluster': totalClusters,
            'edges': {}
        };
        totalClusters += 1;
    graph[v]['edges'][w] = distance;

    if w not in graph:
        graph[w] = {
            'cluster': totalClusters,
            'edges': {}
        };
        totalClusters += 1;
    graph[w]['edges'][v] = distance;

f.close();

def findClosesClusterPair(g):
    minDistance = -1;
    closestClusters = [-1, -1];
    for v in g:
        vertex = g[v];
        #print v, vertex;
        for e in vertex['edges']:
            #print e, vertex['edges'][e]
            #print g[v]['cluster'], g[e]['cluster']
            if g[v]['cluster'] != g[e]['cluster']:
                distance = vertex['edges'][e];
                #print distance;
                if distance < minDistance or minDistance < 0:
                    minDistance = distance;
                    closestClusters = [vertex['cluster'], g[e]['cluster']];
    #print closestClusters, minDistance;
    return closestClusters;

def findMaxSpacing(g):
    minDistance = -1;
    closestClusters = [-1, -1];
    for v in g:
        vertex = g[v];
        for e in vertex['edges']:
            if g[v]['cluster'] != g[e]['cluster']:
                distance = vertex['edges'][e];
                if distance < minDistance or minDistance < 0:
                    minDistance = distance;
                    closestClusters = [vertex['cluster'], g[e]['cluster']];
    print closestClusters, minDistance;

def mergeClusterPair(g, cluster1, cluster2):
    for v in g:
        if g[v]['cluster'] == cluster2:
            g[v]['cluster'] = cluster1


def kClustering(g, targetClusters, totalClusters):
    while totalClusters > targetClusters:
        # find closes pair in different clusters
        [cluster1, cluster2] = findClosesClusterPair(g);
        # merge their belonging clusters
        if cluster1 != cluster2 and cluster1 >= 0:
            mergeClusterPair(g, cluster1, cluster2);
            totalClusters -= 1;
        print totalClusters;

print totalClusters;
kClustering(graph, targetClusters, totalClusters);
findMaxSpacing(graph);
end = time.time()
elapsed = end - start
print "Elapsed time", elapsed;
# 106 - [413, 164] - 30.7070000172s
