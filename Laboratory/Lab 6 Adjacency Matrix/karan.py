
vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D')]


v_map = {v: i for i, v in enumerate(vertices)}


n = len(vertices)
matrix = [[0 for _ in range(n)] for _ in range(n)]


for start, end in edges:
    row, col = v_map[start], v_map[end]
    matrix[row][col] = 1  

print("   A  B  C  D")
print("----------------")

for i, row in enumerate(matrix):
    print(f"{vertices[i]} | {'  '.join(map(str, row))}")