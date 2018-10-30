
def maxRod(p, n):
    global optimals, count;
    r = 0;
    # if n <= 0:
    #     return 0;
    # if n == 1:
    #     return p[n - 1];
    if n in optimals:
        return optimals[n];
    for i in range(1, n):
        count += 1;
        m = max(p[n - 1], p[i] + maxRod(p, n - i - 1));
        if (m > r):
            r = m;
    optimals[n] = r;
    return r;

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30];
optimals = {
    0: 0,
    1: prices[0],
};
count = 0;
length = 10;

print 'Max revenue for', length, ':', maxRod(prices, length);
print 'Count', count;
