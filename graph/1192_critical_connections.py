""" Critical Connections in a Network
There are n servers numbered from 0 to n - 1 connected 
by undirected server-to-server connections forming a network 
where connections[i] = [ai, bi] represents a connection between servers ai and bi. 

Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.


>>> input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
>>> output: [[1,3]]

>>> input: n = 2, connections = [[0,1]]
>>> output: [[0,1]]
"""

from collections import defaultdict
from typing import List

def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]: 
    ## tarjan으로 풀면 될 듯. 
    disc, low = [-1] * n, [-1] * n 
    self.timestamp = 0
    graph = defaultdict(list)
    bridges = []

    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(node: int, parent: int):
        if disc[node] != -1:
            return 
        
        disc[node] += self.timestamp
        low[node] += self.timestamp
        self.timestamp += 1 
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue 
            
            dfs(neighbor, node)

            low[node] = min(low[neighbor], low[node])
        
            if disc[node] < low[neighbor]:
                bridges.append([node, neighbor])
    
    dfs(0, -1)
    return bridges
        
