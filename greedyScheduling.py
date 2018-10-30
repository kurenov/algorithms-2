###
    # Code by Olzhas Kurenov
    # Implementation of Greedy Task Scheduler
###
print '\n~~~~~~~~~Greedy Task Scheduler~~~~~~~~~\n'

#from operator import itemgetter;

f = open('jobs.txt', 'r');
n = int(f.readline());
jobs = [[0, 0, 0, 0]] * n;
count = 0;
for line in f.readlines():
    w, l = [float(x) for x in line.split()];
    jobs[count] = [w, l, w - l, w / l];
    count+=1;
f.close();

#jobs.sort(key=lambda x: x[2]);
jobs = sorted(jobs, key=lambda x:-x[0]);
jobsByDifference = sorted(jobs, key=lambda x:-x[2]);
jobsByDivision = sorted(jobs, key=lambda x:-x[3]);

totalLength = 0
total = 0
for job in jobsByDifference:
    total = total + job[0] * (job[1] + totalLength);
    totalLength = totalLength + job[1];
print totalLength
print int(total)


totalLength = 0
total = 0
for job in jobsByDivision:
    total = total + job[0] * (job[1] + totalLength);
    totalLength = totalLength + job[1];
print totalLength
print int(total)
