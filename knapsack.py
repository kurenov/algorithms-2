def knapsack(capacity, n):
    global weights, weightValueMap, optimals, count;
    if n <= 0:
         return 0;
    if n in optimals:
        return optimals[n];
    last = weights[n - 1];
    for i in range(0, n):
        r = 0;
        m = 0;
        weight = weights[i];
        print last, weight
        c = capacity - weight;
        if last > capacity and weight <= capacity:
            m = weightValueMap[weight] + knapsack(c, n - i - 1);
        elif  last <= capacity and weight > capacity:
            m = weightValueMap[last];
        elif last <= capacity and weight <= capacity:
            m = max(weightValueMap[last], weightValueMap[weight] + knapsack(c, n - i - 1));
        if (m > r):
            r = m;
    optimals[n] = r;
    return r;

f = open('knapsack0.txt', 'r');
weights = [];
weightValueMap = {};
optimals = {};
capacity, n = [int(x) for x in f.readline().split()];
for line in f.readlines():
    value, weight = [int(x) for x in line.split()];
    weights.append(weight);
    weightValueMap[weight] = value;

weights = sorted(weights);
print weights;
print weightValueMap;

count = 0;
length = 10;

print 'knapsack', capacity, ':', knapsack(capacity, len(weights));
print optimals;
# print 'Count', count;
# 104696 - x
# 2042603 - x
# 3733600 - x
