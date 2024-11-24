def main():
    edges_count = 0
    with open("cost239", mode="r", encoding="utf8") as file:
        nodes_count = int(file.readline().strip())
        graph = [[0 for _ in range(nodes_count)] for _ in range(nodes_count)]
        while True:
            line = file.readline()
            if line == "":
                break
            begin, end, weight = tuple(map(int, line.strip().split()))
            graph[begin][end] = weight
            graph[end][begin] = weight
            edges_count += 1


if __name__ == "__main__":
    main()