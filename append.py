'''fp = open("graph.txt", 'a')
graph = []
graph.append(2)
graph.append(7)
for i in range(len(graph)):
    fp.write(',' + str(graph[i]))
fp.close()'''
graph = [-1,1]
with open('graph.txt') as f:
    for line in f:
        values = line.split(',')
        graph.append(int(values[-1]))
        break

print(graph)