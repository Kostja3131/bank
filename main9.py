import heapq

# Представление графа в виде списка смежности
graph = {
    'a': [('b', 3), ('c', 6), ('d', 4)],
    'b': [('a', 3), ('c', 2), ('e', 8)],
    'c': [('a', 6), ('b', 2), ('d', 7), ('e', 2), ('f', 4)],
    'd': [('a', 4), ('c', 7), ('f', 3), ('g', 12)],
    'e': [('b', 8), ('c', 2), ('f', 3), ('h', 3)],
    'f': [('c', 4), ('d', 3), ('e', 3), ('g', 5), ('h', 2)],
    'g': [('d', 12), ('f', 5), ('h', 6)],
    'h': [('e', 3), ('f', 2), ('g', 6)],
}

def prim(graph, start):
    mst = []  # Список для хранения рёбер MST
    visited = set()  # Посещённые вершины
    min_heap = []  # Мин-куча для выбора минимального ребра

    # Добавляем все рёбра стартовой вершины в кучу
    visited.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))

    while min_heap:
        # Извлекаем ребро с минимальным весом
        weight, frm, to = heapq.heappop(min_heap)
        if to not in visited:
            # Добавляем ребро в MST
            mst.append((frm, to, weight))
            visited.add(to)

            # Добавляем новые рёбра, выходящие из текущей вершины
            for neighbor, weight in graph[to]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, to, neighbor))

    return mst

# Запуск алгоритма Прима
start_node = 'a'
mst_result = prim(graph, start_node)

# Вывод минимального остовного дерева
print("Минимальное остовное дерево (MST):")
for edge in mst_result:
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")
