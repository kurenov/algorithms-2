###
    # Code by Olzhas Kurenov
    # Faster Implementation of a Greedy k-Clustering Algorithm
    # Running time: O(n + m)
###
import time;
print '\n~~~~~~~~~Greedy k-Clustering Algorithm~~~~~~~~~\n';

start = time.time()

def readData(fileName):
    global totalClusters, edges, vertexClusterMap;
    edgeCounter = 0;
    f = open(fileName, 'r');
    totalClusters = int(f.readline());
    for line in f.readlines():
        v, w, distance = [int(x) for x in line.split()];
        edges.append([v, w, distance]);
        vertexClusterMap[edgeCounter] = edgeCounter;
        edgeCounter += 1;
    f.close();
    edges = sorted(edges, key=lambda item: item[2]);

def findClosestClusterPair():
    global edges, vertexClusterMap, cursor;
    [v, w, distance] = edges[cursor];
    cluster1 = vertexClusterMap[v];
    cluster2 = vertexClusterMap[w];
    cursor += 1;
    return [cluster1, cluster2];

def mergeClusterPair(cluster1, cluster2):
    global vertexClusterMap, totalClusters;
    if cluster1 != cluster2:
        for v in vertexClusterMap:
            if vertexClusterMap[v] == cluster2:
                vertexClusterMap[v] = cluster1;
        totalClusters -= 1;

def kClustering(targetClusters):
    global totalClusters;
    print totalClusters, targetClusters;
    while totalClusters > targetClusters:
        # find closes pair in different clusters
        [cluster1, cluster2] = findClosestClusterPair();
        # merge their belonging clusters
        mergeClusterPair(cluster1, cluster2);

def findMaxSpacing(edges, cursor):
    while cursor < len(edges):
        [v, w, distance] = edges[cursor];
        cursor += 1;
        cluster1 = vertexClusterMap[v];
        cluster2 = vertexClusterMap[w];
        if cluster1 != cluster2:
            print [cluster1, cluster2, distance];
            return [cluster1, cluster2, distance];

cursor = 0;
clusters = {};
edges = [];
vertexClusterMap = {};
totalClusters = 0;
targetClusters = 4;

readData('clustering1.txt');
kClustering(targetClusters);
findMaxSpacing(edges, cursor);

print cursor;
end = time.time();
elapsed = end - start;
print "Elapsed time", elapsed;
# 106 - [414, 165] - 4.41999983788s
