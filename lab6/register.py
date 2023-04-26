"""
file: register.py
CSCI-665: Hw 6 Problem 3 Solution
Authors: Deepika Kini, Adith Shetty
language: python3
Description: Using the max flow problem we figure out the courses
that need to be assigned to students.
"""

import sys

def dfs(graph, start, sink, previous, count_nodes, track_path , visited):
    """
    Calculates the path that exists between start and sink and appends the path
    nodes into track_path
    :param graph: the graph
    :param start:the start node
    :param sink: the target node
    :param previous: the node from which the path needs to be considered
    :param count_nodes:the total count of nodes
    :param track_path: the path from start to sink
    :param visited: the visited nodes to avoid circular movement
    :return: returns if path exists
    """
    # print(start, previous, sink, track_path, min)

    for i in range(len(graph[previous])):
        # print(i)
        if graph[previous][i] > 0 and i!= start and visited[i]==0:
            visited[i] = 1
            if i == sink:
                track_path.append(i)
                # print(track_path)
                # if graph[previous][i] < min:
                #     min = graph[previous][i]
                return True
            flag = dfs(graph, start, sink, i, count_nodes, track_path, visited)
            # print(track_path)
            if flag:
                track_path.append(i)
                # if graph[previous][i] < min:
                #     min = graph[previous][i]
                return True

    return False




def FF(graph, source, sink, count_nodes): #O(mC)=> O(m*n) since C is less than equal to 3*n
    """
    The main logic for max flow problem (Ford Fulkerson algorithm) resides here.
    We use the graph to find path(use dfs) and create residual graphs for next iteration.

    :param graph: the graph
    :param source: the start node
    :param sink:the final node
    :param count_nodes:the no. of nodes
    :return:None
    """

    # This array is filled by BFS and to store path

    track_path=[]
    # print(count_nodes)
    visited = [0 for _ in range(count_nodes)]
    visited[0] = 1
    # print(dfs(graph, source, sink,source, count_nodes, track_path, visited))

    count = 0
    while dfs(graph, source, sink,source, count_nodes, track_path, visited):
        track_path.append(0)
        # print(track_path)
        # Augment the flow while there is path from source to sink
        for j in range(len(track_path)-1):
            # print(j, j+1)
            # print(graph[track_path[j+1]][track_path[j]])
            graph[track_path[j+1]][track_path[j]]-= 1
            if track_path[j] != count_nodes - 1 and track_path[j+1] != 0 :
                graph[track_path[j]][track_path[j+1]] += 1
        # print(graph)
        track_path = []
        # print(count_nodes)
        visited = [0 for _ in range(count_nodes)]
        visited[0] = 1
        count+=1
    print (count)





if __name__ == '__main__':
    """
    takes the input and creates a matrix to work with.
    It adds a start and sink node to run the max flow problem algorithm
    Then it calls Ford Fulkerson algorithm
    :return: None
    """
    # count of students and courses
    s, c = map(int, input().split())
    network = []
    start_node = []

    #make a matrix to store edge details (forward and backward)
    graph = [[0 for _ in range(s+c+2)] for _ in range(s+c+2)]


    for i in range(s):
        graph[0][i+1] = 3

    # adding course connection to students
    for i in range(s):
        list_of_courses_for_student = []
        list_of_courses_for_student = list(map(int, input().strip().split()))

        c_count = len(list_of_courses_for_student)
        temp = []
        # print(list_of_courses_for_student, c_count)
        for j in range(c_count):
            graph[i + 1][list_of_courses_for_student[j]+s] = 1

    for j in range(c):
        graph[s+j+1][-1] = int(input())
    # print(graph)


# print(len(graph)-1)

source = 0
sink = len(graph) -1

FF(graph,source, sink, len(graph))

