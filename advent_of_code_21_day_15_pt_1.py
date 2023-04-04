import copy
from collections import defaultdict

input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

for i in range(0, len(input)):
    input[i] = list(input[i])
    for j in range(0, len(input[i])):
        input[i][j] = int(input[i][j])

end_y = len(input) - 1
end_x = len(input[0]) - 1

start_y = 0
start_x = 0

def dijkstra(input, start_y, start_x, end_y, end_x):
    visited = set()
    pq = [[0, start_y, start_x]]
    node_costs = defaultdict(lambda: float('inf'))
    node_costs[str([start_y, start_x])] = 0
    while len(pq) > 0:
        temp = []
        for j in range(0, len(pq)):
            node = pq[j]
            visited.add(str([node[1], node[2]]))
            adj = []
            if node[1] == 0 and node[2] == 0:
                adj.append([node[1] + 1, node[2]])
                adj.append([node[1], node[2] + 1])
            elif node[1] == 0 and node[2] == len(input[0]) - 1:
                adj.append([node[1] + 1, node[2]])
                adj.append([node[1], node[2] - 1])
            elif node[1] == len(input) - 1 and node[2] == len(input[0]) - 1:
                adj.append([node[1] - 1, node[2]])
                adj.append([node[1], node[2] - 1])
            elif node[1] == len(input) - 1 and node[2] == 0:
                adj.append([node[1] - 1, node[2]])
                adj.append([node[1], node[2] + 1])
            elif node[1] == 0 and node[2] > 0 and node[2] < len(input[0]) - 1:
                adj.append([node[1] + 1, node[2]])
                adj.append([node[1], node[2] + 1])
                adj.append([node[1], node[2] - 1])
            elif node[1] > 0 and node[1] < len(input) - 1 and node[2] == len(input[0]) - 1:
                adj.append([node[1] + 1, node[2]])
                adj.append([node[1] - 1, node[2]])
                adj.append([node[1], node[2] - 1])
            elif node[1] == len(input) - 1 and node[2] > 0 and node[2] < len(input[0]) - 1:
                adj.append([node[1] - 1, node[2]])
                adj.append([node[1], node[2] + 1])
                adj.append([node[1], node[2] - 1])
            elif node[1] > 0 and node[1] < len(input) - 1 and node[2] == 0:
                adj.append([node[1] + 1, node[2]])
                adj.append([node[1] - 1, node[2]])
                adj.append([node[1], node[2] + 1])
            else:
                adj.append([node[1] + 1, node[2]])
                adj.append([node[1] - 1, node[2]])
                adj.append([node[1], node[2] + 1])
                adj.append([node[1], node[2] - 1])
            for i in range(0, len(adj)):
                if str(adj[i]) in visited: 
                    continue
                new_cost = node[0] + input[adj[i][0]][adj[i][1]]
                if node_costs[str(adj[i])] > new_cost:
                    node_costs[str(adj[i])] = new_cost
                    temp.append([new_cost, adj[i][0], adj[i][1]])
        pq = copy.deepcopy(temp)
    return node_costs[str([end_y, end_x])]

result = dijkstra(input, start_y, start_x, end_y, end_x)

print('result:', result)




