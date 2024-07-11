def BFS(start,graph):
    visted =[start]
    q=[start]
    while len(q)!=0:
        ele=q.pop(0)
        for i in graph[ele]:
            if i not in visted:
                q.append(i)
                visted.append(i)
    return visted
def DFS(start,graph,visited):
    visited.append(start)
    for ne in graph[start]:
        if ne not in visited:
            DFS(ne,graph,visited)
    return visited
            
graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["B","A","E"],
    "D":["B","E"],
    "E":["D","C"]
}
print(BFS("A",graph))
print(DFS("C",graph,[]))