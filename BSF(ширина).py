#Breadth First Search

matrix = [[0,1,1,0,0],       #матрица смежности, задающая граф
          [1,0,0,1,0],
          [1,0,0,0,0],
          [0,1,0,0,1],
          [0,0,0,1,0]]
"""
    Данный граф выглядит так:
                    1
                   / \
                  2   3
                 / 
                4   
               /
              5 
"""
visited = [0] * len(matrix)  #список уровней вершин, 0 - для непосещенных вершин
stack = []                   #создадим список (стэк) для очереди

def BFS(top):
    stack.append(top)        #добавим в очередь
    visited[top] = 1         #1 - уже для посещенной вершины
    while (len(stack)):
        point = stack.pop(0) #берем очередную вершину из стэка
        for i in range(1, len(matrix) + 1):        #положим в стэк непосещенные и связанные с данной вершины
            if (visited[i - 1] == 0) and (matrix[point - 1][i - 1] == 1):
                stack.append(i)
                visited[i - 1] = visited[point] + 1

                
    for j in range(len(visited)): #проверка на случай несвязного графа, переберем непосещенные вершины
        if (visited[j] == 0):
            BFS(j)
