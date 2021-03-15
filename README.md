# BFS-example
- BFS(Breadth First Search) 너비 우선 탐색을 최대한 쉽게 이해하기 위한 샘플 프로그램입니다.
- Python3 로 작성되었습니다.

***
![image](https://user-images.githubusercontent.com/72640840/111106342-48edcf80-8598-11eb-886d-5a9b30cb78dc.png)
- 위와 같은 트리가 있다면, 1번 노드부터 번호 순대로 탐색하는 것이 너비우선 탐색입니다.
- 이 탐색을 하기 위해서는 Queue 자료구조를 사용하여 쉽게 구현할 수 있습니다.

![image](https://user-images.githubusercontent.com/72640840/111106448-818da900-8598-11eb-98a9-d15174325ed3.png)
- 탐색을 시작하고자 하는 노드를 Enqueue 합니다.
- 1번 노드부터 탐색하고자 합니다.

![image](https://user-images.githubusercontent.com/72640840/111106577-aeda5700-8598-11eb-828b-9fc2c5081636.png)
- 1번을 Dequeue 합니다
- 탐색 후엔 Visit 리스트에 넣어줍니다. 중복해서 Enqueue하지 않도록 체크용도로 필요하기 때문입니다.
- 인접한 노드인 2, 3번을 Enqueue합니다.


![image](https://user-images.githubusercontent.com/72640840/111106840-28724500-8599-11eb-922c-d179224258d8.png)
- 2번 노드를 Dequeue 합니다
- 탐색 후엔 Visit 리스트에 넣어줍니다.
- 인접한 노드인 1, 4, 5번을 Enqueue합니다.
- 하지만 1번은 이미 Visit 했으므로 넣지 않습니다.

![image](https://user-images.githubusercontent.com/72640840/111107042-869f2800-8599-11eb-9e98-4125ee3e9f88.png)
- 위와 같이 됩니다.
- 이제 탐색이 완료될 때까지 반복하면 됩니다

![image](https://user-images.githubusercontent.com/72640840/111107225-d382fe80-8599-11eb-9d57-280e7ea6d53f.png)
- 3을 Dequeue 합니다
- 탐색 후엔 Visit 리스트에 넣어줍니다.
- 인접한 6, 7 Enqueue 합니다. 

![image](https://user-images.githubusercontent.com/72640840/111107289-ed244600-8599-11eb-9471-aca5fc5c4611.png)
- 4를 Dequeue 합니다.
- 탐색 후엔 Visit 리스트에 넣어줍니다.
- 인접한 8, 9 Enqueue 합니다

![image](https://user-images.githubusercontent.com/72640840/111107502-44c2b180-859a-11eb-88ce-285cf40fa8cc.png)
- 5를 Dequeue 합니다
- 탐색 후엔 Visit 리스트에 넣어줍니다
- 인접한 10, 11 Enqueue 합니다

![image](https://user-images.githubusercontent.com/72640840/111107554-6459da00-859a-11eb-9a2e-063ba07e36f3.png)
- 6을 Dequeue 합니다
- 탐색 후엔 Visit 리스트에 넣어줍니다
- 인접한 12 13 Enqueue 합니다

![image](https://user-images.githubusercontent.com/72640840/111107597-7c315e00-859a-11eb-942d-d10da9a78b3e.png)
- 7을 Dequeue 합니다
- 탐색 후엔 Visit 리스트에 넣어줍니다
- 인접한 14 Enqueue 합니다

![image](https://user-images.githubusercontent.com/72640840/111107638-953a0f00-859a-11eb-9184-c361270b4b1a.png)
- 이제 탐색할 것이 없으니 나머지들을 빼버리면 탐색이 완료됩니다.

***
## 소스

```python
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
```
## 결과
![image](https://user-images.githubusercontent.com/72640840/111107818-efd36b00-859a-11eb-849a-c13945129517.png)

