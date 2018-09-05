matrix = [[0,1,1,0,0],       #матрица смежности, задающая граф
          [1,0,0,1,0],
          [1,0,0,0,0],
          [0,1,0,0,1],
          [0,0,0,1,0]] 
visited = [0] * len(matrix)  #список уровней вершин
stack = []                   #создадим список (стэк) для очереди

def BFS(top):
    stack.append(top)
    visited[top] = 1
    while (len(stack)):
        point = stack.pop(0) #берем очередную вершину
        for i in range(1, len(matrix) + 1):
            if (visited[i - 1] == 0) and (matrix[point - 1][i - 1] == 1):
                stack.append(i)
                visited[i - 1] = visited[point] + 1

                
    for j in range(len(visited)): #проверка на случай несвязного графа
        if (visited[j] == 0):
            BFS(j)
    
            
BFS(4)                      #ввод номер стратовой вершины (произвольно)
print(min(visited))
