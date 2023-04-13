"""
file: spies.py
CSCI-665: Hw 5 Problem 3 Solution
Authors: Deepika Kini, Adith Shetty
language: python3
Description: This program computes the minimum number of channels required
between the spies and avoiding keeping the unreliable ones as intermediate spies
Assumed that weights can be negative
We first find MST for reliable nodes and then add the best edge from
reliable to the unreliable ones
"""
import sys


def prim(matrix, node_count, unrel_array, unrel_count):
    """
    The algorithm used for MST is prim's algorithm using 2d matrix (O(n^2))
    :param matrix: the graph
    :param node_count: nodes in graph
    :param unrel_array:array with boolean holding whether node is unreliable
    :param unrel_count: count of unreliable nodes in graph
    :return: cost of edges in MST
    """
    #cost array to keep min cost for each node
    T = []
    cost = [sys.maxsize for i in range(node_count)]
    #parent array keeps track of the connecting node with least code to the node
    parent = [None for i in range(node_count)]

    visited = [False for _ in range(node_count)]

    #start with a reliable node
    i = 0
    while unrel_array[i]:
        i+= 1
    #initialize values for the start node
    cost[i] = 0
    visited[i] = True
    current_node = i
    edge_count = 0
    flag_none = False
    #for each reliable node with an edge to reliable unvisited node,
    # evaluate if it is the least costing one
    #done for the first node
    for i in range(node_count):
        if matrix[current_node][i] > -sys.maxsize and cost[i] > matrix[current_node][i] \
                and not unrel_array[i] and not visited[i]:
            #keep track of best cost edge for each node and the new parent
            cost[i] = matrix[current_node][i]
            parent[i] = current_node


    #find best node in the new iteration until maximum edges added (without cycle being formed)
    while edge_count < (node_count - 1 - unrel_count):
        min_cost = sys.maxsize
        current_node = None
        for min_finder in range(len(cost)):
            if not visited[min_finder] and not unrel_array[min_finder]:
                if min_cost > cost[min_finder]:
                    min_cost = cost[min_finder]
                    current_node = min_finder
        #break if there is no visited node with an edge for next iteration
        if min_cost == sys.maxsize:
            flag_none =True
            break
        #add new node to visited set and link to T
        #increase edge count
        T.append(list([current_node,parent[current_node]]))
        visited[current_node] = True
        edge_count += 1

        #update the
        for i in range(node_count):
            if matrix[current_node][i] > -sys.maxsize and cost[i] > matrix[current_node][i] \
                    and not unrel_array[i] and not \
            visited[i]:
                cost[i] = matrix[current_node][i]
                parent[i] = current_node

    # print(T)
    total_cost = 0

    if flag_none:
        return None
    else:
        for i in range(len(T)):
            # print(T[i])
            total_cost += matrix[T[i][0]][T[i][1]]
    # print(total_cost)

    # handling the unreliable node cases
    for i in range(len(unrel_array)):
        if unrel_array[i]:
            #print(i,unrel_array[i])
            min = sys.maxsize
            #print(matrix[i])
            for j in range(len(matrix[i])):
                #avoid edges to unreliable nodes
               if matrix[i][j]!= -sys.maxsize and not unrel_array[j]  and min > matrix[i][j]:
                   min = matrix[i][j]
            #print(min)
            #if the best cost(if present), add total_cost
            if min < sys.maxsize :
                #print("total cost", total_cost)

                total_cost += min
            else:
                flag_none =True
                break
    #return None for bad cases else total_count
    if flag_none:
        return None
    else:
        return total_cost





if __name__ == '__main__':
    """
    takes the input and populates a 2D matrix with the edge information
    Calls the prim algorithm to get the minimum spanning graph
    :return: None
    """
    node_count, edge_count = (map(int, input().strip().split()))
    # #print(node_count, edge_count,"node and edge")
    unrel_count = int(input())
    #print(node_count, edge_count, unrel_count, "node and edge and unrel")
    unreliable_nodes = (list(map(int, input().strip().split())))
    unreliable_arr = [0 for i in range(node_count)]
    for i in range(unrel_count):
        unreliable_arr[unreliable_nodes[i]] = 1

    # print("unrel array",unreliable_arr)
    #print(unreliable_nodes)
    edges = []
    for i in range(edge_count):
        edges.append(list(map(int, input().strip().split())))
    #print(edges)

    # assuming weights can be negative
    matrix = [[-sys.maxsize for _ in range(node_count)] for _ in range(node_count)]  # O(n^2)

    for i in range(edge_count):
        #bidirectional edges added
        matrix[edges[i][0]][edges[i][1]] = edges[i][2]
        matrix[edges[i][1]][edges[i][0]] = edges[i][2]

    #cost of edges in MST
    val = prim(matrix,node_count, unreliable_arr, unrel_count)
    if val ==  None:
        print("NONE")
    else:
        print(val)