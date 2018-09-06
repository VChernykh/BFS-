#Breadth First Search

matrix = [[0,1,1,0,0],                #матрица смежности, задающая граф
          [1,0,0,1,0],
          [1,0,0,0,0],
          [0,1,0,0,1],
          [0,0,0,1,0]] 
visited = [0] * len(matrix)           #список уровней вершин
stack = []                            #создадим список (стэк) для очереди

def BFS(start, end):                  #start - начальная вершина обхода, end - конечная
    stack.append(start)               #добавим в очередь 
    visited[start] = 1                
    while (len(stack)):
        point = stack.pop(0)          #берем очередную вершину
        for i in range(1, len(matrix) + 1):     #положим в стэк непосещенные и связанные с данной вершины
            if (visited[i - 1] == 0) and (matrix[point - 1][i - 1] == 1):
                stack.append(i)
                visited[i - 1] = visited[point] + 1

                
    if(visited[end] == 0):
        return "Not connect"
    else:
        return str(visited[end])
    
            
print(BFS(4, 1))                      #ввод кратчайшего расстояния (в терминах количества рёбер)
