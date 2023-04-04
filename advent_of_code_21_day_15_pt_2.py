import heapq as heap
import copy
from collections import defaultdict
import math

input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

for i in range(0, len(input)):
    input[i] = list(input[i])
    for j in range(0, len(input[i])):
        input[i][j] = int(input[i][j])

initial_len_y = len(input)
initial_len_x = len(input[0])

input_5_col = []

for i in range(5):
    for j in range(0, len(input)):
        input_5_col.append(input[j])

input_5_col_5_row = []

for i in range(0, len(input_5_col)):
    input_5_col_5_row.append([])

for i in range(0, len(input_5_col_5_row)):
    for j in range(5):
        for k in range(0, len(input_5_col[i])):
            input_5_col_5_row[i].append(input_5_col[i][k])

input = copy.deepcopy(input_5_col_5_row)

end_y = len(input) - 1
end_x = len(input[0]) - 1

for i in range(len(input)):
    for j in range(len(input[i])):
        input[i][j] = ((input[i][j] + math.floor(i / initial_len_y) + math.floor(j / initial_len_x) - 1) % 9) + 1

start_y = 0
start_x = 0

def dijkstra(input, start_y, start_x, end_y, end_x):
    visited = set()
    options = []
    heap.heappush(options, [0, start_y, start_x])
    node_costs = defaultdict(lambda: float('inf'))
    node_costs[str([start_y, start_x])] = 0
    while options:
        node = heap.heappop(options)
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
            if str(adj[i]) not in visited: 
                new_cost = node[0] + input[adj[i][0]][adj[i][1]]
                if node_costs[str(adj[i])] > new_cost:
                    node_costs[str(adj[i])] = new_cost
                    heap.heappush(options, [new_cost, adj[i][0], adj[i][1]])
    return node_costs[str([end_y, end_x])]

result = dijkstra(input, start_y, start_x, end_y, end_x)

print('result:', result)