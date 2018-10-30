###
    # Code by Olzhas Kurenov
    # Implementation of Greedy Task Scheduler
    # W1 P1
    # 1: 69119377652
    # 2: 67311454237
###

print '\n~~~~~~~~~Greedy Task Scheduler~~~~~~~~~\n'

# Compares jobs based on score=w-l
# if two scores are the same compares by weight
def comparerDifference(a, b):
    # print a, b
    if (a[2] == b[2]):
        return b[0] - a[0]
    else:
        return b[2] - a[2]

def computeWeightedTotal(jobs):
    weightedCompletionTime = 0
    time = 0
    for job in jobs:
        weightedCompletionTime += job[0] * (job[1] + time)
        time += job[1]
    return weightedCompletionTime

# IO
f = open('jobs.txt', 'r')
n = int(f.readline())

# preallocating memory
jobs = [[0, 0, 0, 0]] * n
index = 0

# reading the input
for line in f.readlines():
    w, l = [float(x) for x in line.split()]
    jobs[index] = [int(w), int(l), int(w - l), w / l]
    index += 1
f.close()

# sort by difference score
jobsByDifference = sorted(jobs, cmp=comparerDifference)
print computeWeightedTotal(jobsByDifference)

# sort by precomputed division score
jobsByDivision = sorted(jobs, key=lambda x:-x[3])
print computeWeightedTotal(jobsByDivision)