"""
    Depth First Search
    start - НАЧАЛЬНАЯ ВЕРШИНА (кортеж): start = {'1': ('2','5')}
    peaks - СЛОВАРЬ ВЕРШИН (словарь кортежей): peaks = {'1':('2','5'), '2':('3','4'), '3':(), '4':(), '5':()}.
    peak - ЭЛЕМЕНТ СЛОВАРЯ - ВЕРШИНА (кортеж)
    done - СПИСОК ПОСЕЩЕННЫХ ВЕРШИН (список)
    point - ЭЛЕМЕНТЫ PEAK, вершины соединенные с peak

    Данный граф выглядит так:
                             5
                             |  
                             1 - 2 - 3
                                 |        
                                 4       
                

    peaks = {'1':('2','5'), '2':('3','4'), '3':(), '4':(), '5':()}
    
"""


def DFS(start, peaks, done):
    for peak, point in start.items():
        
        if peak not in done:
            yield peak, point
            done.append(peak)
            for i in point:
                
                new_point={ i : peaks[i]}
                
                for point in DFS(new_point, peaks, done):
                    
                    if point not in done:
                        yield done
