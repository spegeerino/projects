from numpy import Infinity
NO_EDGE = Infinity 
small_graph = []
small_graph.append([NO_EDGE,16,12,21,NO_EDGE,NO_EDGE,NO_EDGE])
small_graph.append([16,NO_EDGE,NO_EDGE,17,20,NO_EDGE,NO_EDGE])
small_graph.append([12,NO_EDGE,NO_EDGE,28,NO_EDGE,31,NO_EDGE])
small_graph.append([21,17,28,NO_EDGE,18,19,23])
small_graph.append([NO_EDGE,20,NO_EDGE,18,NO_EDGE,NO_EDGE,11])
small_graph.append([NO_EDGE,NO_EDGE,31,19,NO_EDGE,NO_EDGE,27])
small_graph.append([NO_EDGE,NO_EDGE,NO_EDGE,23,11,27,NO_EDGE])

big_graph = []
data_file = open("p107_network.txt", "r")
line = data_file.readline()
while line:
    sanitize = lambda x: int(x) if int(x) != 0 else NO_EDGE
    nums = [sanitize(i) for i in line.split(",")]
    big_graph.append(nums)
    line = data_file.readline()
def mst_savings(graph):
    '''
    input: a graph represented as a vertex by vertex matrix A, 
    with a weighted edge between vertex i and vertex j represented as
    the weight of the edge at entries A_ij and A_ji.

    output: the potential weight saved by reducing the graph to its minimal spanning tree
    and eliminating all the unnecessary edges.

    Runs in O(n^2), where n is the number of vertices.
    '''
    assert len(graph) == len(graph[0]), "matrix representing graph is not valid"
    #find the initial weight
    init_weight = 0
    for i in graph:
        for j in i:
            if j != NO_EDGE:
                init_weight += j
    init_weight //= 2 # double counted edges (change to float div if you want to use with floats)
    #start with the first vertex (doesn't matter where you start)
    mst_vertices = [0]
    mst_weight = 0
    #iterate until all verties are added to mst
    while len(mst_vertices) < len(graph):
        min_weight = Infinity
        min_to_add_v = -1
        # find minimum weight edge that is connected to the current mst and a new vertex
        for w in mst_vertices:
            for v in range(len(graph[w])):
                if v not in mst_vertices:
                    if graph[w][v] < min_weight:
                        min_weight = graph[w][v]
                        min_to_add_v = v
        # the minimum weight edge is between v and w, now add to tree
        mst_vertices.append(min_to_add_v)
        mst_weight += min_weight
    return init_weight - mst_weight

print(mst_savings(small_graph))
print(mst_savings(big_graph))