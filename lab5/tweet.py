"""
file: tweet.py
CSCI-665: Hw 5 Problem 3 Solution
Authors: Deepika Kini, Adith Shetty
language: python3
Description: An O(m+n) algorithm that determines the minimum number of individuals that
must be provided with an initial item to “tweet” to guarantee that all the individuals
in the network end up “tweeting” or “retweeting” the item.
"""
import sys

#changing config to accomodate the last test case
sys.setrecursionlimit(3000)

def dfs(network, visited, finish_time, node, finish_count):
    """

    :param network: the graph to traverse
    :param visited: visited array
    :param finish_time: finish time array to keep track of
                    when node was removed from consideration
    :param node: node under consideration
    :param finish_count: count to keep track
    :return: finish count
    """

    for i in range(len(network[node])):
        #print(network[node][i])
        if not visited[network[node][i]]:
            visited[network[node][i]] = True
            finish_count = dfs(network, visited, finish_time, network[node][i], finish_count)
    #finish time provided for node after all children traversed
    finish_time.append(node)
    finish_count += 1

    return finish_count

if __name__ == '__main__':
    """
    takes the input and creates the adjaceny list to work with.
    Gets the SCC groups and checks for inter-connectivity in the DAG
    
    :return: None
    """

    #take node count for looping to create network and inverted_network
    node_count = int(input())
    incoming = [True for _ in range(node_count)]
    #has the node numbers that follow the node (index)
    network = []
    #inverts the edges for inverted graph
    inverted_network = [[] for _ in range(node_count)]
    #print(node_count, edge_count,"node and edge")

    #takes the edge details
    for i in range(node_count):
        current_connections = list(map(int,input().strip().split()))
        if len(current_connections) == 1:
            incoming[i] = False
        for j in range(len(current_connections) - 1):
            inverted_network[current_connections[j]].append(i)
        network.append(current_connections[:-1])
    #print(network)
    #print(inverted_network)

    #################
    #scc calculation

    visited = [False for _ in range(node_count)]
    finish_time = []

    #step1: dfs with finish time for network
    finish_count = 1
    for i in range(node_count):
        if not visited[i]:
            visited[i] = True
            finish_count = dfs(network, visited, finish_time, i, finish_count)

    decreased_finish_time = finish_time[::-1]



    #step2: DFS with finishing time for reverse graph using descending finish time of step1
    #also creates the groups of SCC and
    visited = [False for _ in range(node_count)]

    finish_count = 1
    scc= []
    scc_group = [0 for _ in range(node_count)]
    scc_group_count = 1

    #O(m+n)
    for i in range(len(decreased_finish_time)):
        #only takes nodes not visited from decreased_finish_time array
        if not visited[decreased_finish_time[i]]:
            finish_time = []
            visited[decreased_finish_time[i]] = True
            finish_count = dfs(inverted_network, visited, finish_time,
                               decreased_finish_time[i], finish_count)
            #groups the nodes in same scc and provides a number in the scc_group
            # array for corresponding nodes/indices
            for i in range(len(finish_time)):
                scc_group[finish_time[i]] = scc_group_count
            scc.append(finish_time)
            scc_group_count += 1
    ################# scc end#################

    #initialise array that tracks if the macro-graphs are connected in topology
    scc_group_interconnection = [0 for _ in range(scc_group_count -1 ) ]
    #print(scc_group_interconnection)

    #keeps track off the non_connected SCCs
    non_connected_macro_nodes = 0

    #the below code computes the connections between different groups of scc
    #to find connections between macro-nodes using adj list
    #O(m+n) going through all edges
    for i in range(len(network)):
        #print(network[i])
        for j in range(len(network[i])):
            #print(scc_group[i], scc_group[network[i][j]])
            if scc_group[i] != scc_group[network[i][j]]:
                #print(True)
                scc_group_interconnection[scc_group[network[i][j]]-1] = 1
    #print(scc_group_interconnection)

    for i in range(len(scc_group_interconnection)):
        if scc_group_interconnection[i] != 1:
            non_connected_macro_nodes+= 1
    print(non_connected_macro_nodes)



