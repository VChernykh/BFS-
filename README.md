# BFS-
<br>Поиск в ширину (англ. Breadth-First Search, BFS) позволяет вычислить кратчайшие расстояния (в терминах количества рёбер) от выделенной вершины ориентированного графа до всех остальных вершин, и/или построить корневое направленное дерево, расстояния в котором совпадают с расстояниями в исходном графе.
<br>
<br>
<b>Описание:</b>
- Поместить узел, с которого начинается поиск, в изначально пустую очередь.
- Извлечь из начала очереди узел u и пометить его как развёрнутый.
- Если узел u является целевым узлом, то завершить поиск с результатом «успех».
- В противном случае, в конец очереди добавляются все преемники узла {\displaystyle u} u, которые ещё не развёрнуты и не находятся в очереди.
- Если очередь пуста, то все узлы связного графа были просмотрены, следовательно, целевой узел недостижим из начального; завершить поиск с результатом «неудача».
- Вернуться к п. 2.
