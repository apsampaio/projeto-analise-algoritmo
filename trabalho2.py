import heapq


def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def main():
    M, _, _, C = map(int, input().split())
    graph = {i: {} for i in range(M + 1)}
    graph_imp = {i: {} for i in range(M + 1)}

    aux = input().split()
    for i in range(0, len(aux), 3):
        U, V, D = aux[i:i+3]
        U, V, D = int(U), int(V), float(D)

        graph[U][V], graph_imp[U][V] = D, D
        graph[V][U], graph_imp[V][U] = D, D

    aux = list(map(int, input().split()))
    for i in range(0, len(aux), 2):
        U, V = aux[i:i+2]

        if V in graph_imp[U]:
            if graph_imp[U][V] > 1:
                graph_imp[U][V] = 1
                graph_imp[V][U] = 1
        else:
            graph_imp[U][V] = 1
            graph_imp[V][U] = 1

    button_room = 0
    your_distances = dijkstra(graph, button_room)
    impostor_distances = dijkstra(graph_imp, button_room)

    for _ in range(C):
        encounter = int(input())
        if your_distances[encounter] > impostor_distances[encounter]:
            print("defeat")
        else:
            print("victory")


if __name__ == "__main__":
    main()
