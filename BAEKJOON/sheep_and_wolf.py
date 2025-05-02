def solve(node):
    pass

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
e = len(edges)
left = [0] * (e+2)
right = [0] * (e+2)
for i in range(0, e-1, 2):
    parent = edges[i][0]
    child = edges[i][1]

