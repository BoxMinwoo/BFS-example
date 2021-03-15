graph = {
    0 : set([1]),
    1 : set([0, 2, 3]),
    2 : set([1, 3, 4]),
    3 : set([1, 2, 4, 5]),
    4 : set([2, 3]),
    5 : set([3, 6, 7]),
    6 : set([5, 8]),
    7 : set([5]),
    8 : set([6])
}

def BFS(graph, startNode) :
    visit = list()
    queue = list()
    
    queue.append(startNode)
    
    while queue :
        node = queue.pop(0)
      
        if node not in visit : # 노드가 없을 때만 추가합니다
            visit.append(node)
            queue.extend(graph[node])
            
    return visit

BFS(graph, 0)