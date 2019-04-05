#!/usr/bin/python3
#
# Author: Brandon Niblock
# Assignment: Bellman-Ford algorithm
# Pseudocode reference: https://brilliant.org/wiki/bellman-ford-algorithm/#algorithm-psuedo-code
#for v in V:  #my comment for each node all of the nodes
#    v.distance = infinity #my commentset the nodes distance to infinity as a link has not yet been created
#    v.p = None #my commentset the previous node that the node is linked to to None
#source.distance = 0 #my comment sets the source distance to 0 as the distance from the source node to itself is 0
#for i from 1 to |V| - 1: #my comment for all (nodes-1) so that the last node isnt checked with an out of bounds error
#    for (u, v) in E: #must check every node with all of its neighbors
#        relax(u, v)
#relax(u, v):
#    if v.distance > u.distance + weight(u, v): #if this is the minimum distance
#        v.distance = u.distance + weight(u, v) # set the new distance
#        v.p = u # predecessor is the previous node
import math
def main():
    #given distances
    distances = {
        'U': {'Y': 2, 'V': 1},
        'V': {'U': 1, 'V': 3, 'Z': 6},
        'Y': {'U': 2, 'X': 3},
        'X': {'Y': 3, 'V': 3, 'Z': 2},
        'Z': {'V': 6, 'X': 2}}
    start = 'Z'  #starting node  
    #v.distance
    destination = {} 
    #v.p
    predecessor = {}
    for node in distances:
        destination[node] = math.inf 
        predecessor[node] = None
    #sets start node to 0    
    destination[start] = 0 
    #for all nodes -1 to prevent out of bounds error
    for x in range(0, len(distances)-1): 
            #must check ever node with all of its neighbors
            for node in distances:
                for neighbour in distances[node]: #For each neighbour 
                    minimize(node, neighbour, distances, destination, predecessor) 
    #finds which node is connected to the starting node
    for node in predecessor.keys():
        if(predecessor[node] == start):
            end = node     
    print('FORWARDING TABLE')
    print('U:    ('+ start + ',' + end + ')')
    print('V:    ('+start+ ','+ end + ')')
    print('X:    ('+start+ ','+ end + ')')
    print('Y:    ('+start+ ','+ end + ')')
    print('Z:    ('+start + ','+ end + ')')    

    print('Costs')
    print(destination)            
def minimize(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # Record this lower distance
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node
main()                        

