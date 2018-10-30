###
    # Code by Olzhas Kurenov
    # Faster Implementation of a Greedy k-Clustering Algorithm
    # Running time: O(n + m)
###
import time;
import copy;
print '\n~~~~~~~~~Greedy k-Clustering Algorithm~~~~~~~~~\n';

start = time.time()

def readData(fileName):
    global totalClusters, nodes, bitsPerNode;
    nodes = {};
    f = open(fileName, 'r');
    totalClusters, bitsPerNode = [int(x) for x in f.readline().split()];
    #print totalClusters, bitsPerNode;
    counter = 0;
    #for line in f.readlines():
    totalClusters = 20000;
    for i in range(1, totalClusters):
        line = f.readline();
        bits = line.split();
        bitsString = ''.join(bits);
        key = int(bitsString, 2);
        nodes[key] = bits;
        vertexClusterMap[key] = key;
        clusters[key] = [key];
        counter += 1;
    f.close();
    print counter;
    print len(nodes);
    print len(vertexClusterMap);

def flipBit(bit):
    if bit == '0' or bit == 0:
        return '1';
    return '0';

def findAdjacentNodes(bitsArray):
    global bitsPerNode, nodes;
    foundNodes = [];
    for i in range(bitsPerNode):
        bits = copy.copy(bitsArray);
        bits[i] = flipBit(bits[i]);
        key = int(''.join(bits), 2);
        if key in nodes:
            foundNodes.append(key);

    for i in range(bitsPerNode):
        for j in range(i + 1, bitsPerNode):
            bits = copy.copy(bitsArray);
            bits[i] = flipBit(bits[i]);
            bits[j] = flipBit(bits[j]);
            key = int(''.join(bits), 2);
            if key in nodes:
                foundNodes.append(key);
    return foundNodes;

def findAdjacentNodes1(bitsArray):
    global bitsPerNode, nodes;
    foundNodes = [];
    for i in range(bitsPerNode):
        bits = copy.copy(bitsArray);
        bits[i] = flipBit(bits[i]);
        key = int(''.join(bits), 2);
        if key in nodes:
            foundNodes.append(key);
    return foundNodes;

def findAdjacentNodes2(bitsArray):
    global bitsPerNode, nodes;
    foundNodes = [];
    for i in range(bitsPerNode):
        for j in range(i + 1, bitsPerNode):
            bits = copy.copy(bitsArray);
            bits[i] = flipBit(bits[i]);
            bits[j] = flipBit(bits[j]);
            key = int(''.join(bits), 2);
            if key in nodes:
                foundNodes.append(key);
    return foundNodes;

def computeDistance(a, b):
    return sum ( a[i] != b[i] for i in range(len(a)) );

def mergeClusterPair(node1, node2):
    #print [node1, node2];
    global vertexClusterMap, totalClusters;
    cluster1 = vertexClusterMap[node1];
    cluster2 = vertexClusterMap[node2];
    #print cluster1, cluster2;
    if cluster1 != cluster2:
        for v in clusters[node2]:
            if vertexClusterMap[v] != cluster1:
                vertexClusterMap[v] = cluster1;
        clusters[node1] = clusters[node1] + clusters[node2];
        clusters[node2] = [];
        totalClusters -= 1;

def kClustering():
    global totalClusters, nodes;
    count = 0;
    for key in nodes:
        foundNodes = findAdjacentNodes(nodes[key]);
        #print count, '-', key, '-', len(foundNodes), '#', totalClusters;
        count += 1;
        for node in foundNodes:
            mergeClusterPair(key, node);
#
# def kClustering2():
#     global totalClusters, nodes;
#     count = 0;
#     for key in nodes:
#         foundNodes = findAdjacentNodes1(nodes[key]);
#         count += 1;
#         for node in foundNodes:
#             mergeClusterPair(key, node);
#
#     for key in nodes:
#         foundNodes = findAdjacentNodes2(nodes[key]);
#         count += 1;
#         for node in foundNodes:
#             mergeClusterPair(key, node);

clusters = {};
nodes = {};
vertexClusterMap = {};
totalClusters = 0;
bitsPerNode = 0;

readData('clustering_big.txt');
#readData('clusters_implicit_2.txt');
kClustering();
#kClustering2();
print totalClusters;
finalClusters = 0;
for v in clusters:
    if len(clusters[v]) > 0:
        finalClusters += 1;
print finalClusters;

end = time.time();
elapsed = end - start;
print "Elapsed time", elapsed;
# -30k - 220s
# 63204 - 148.875s
