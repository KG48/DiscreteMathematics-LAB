# Vertices and edges
vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')]

# Map vertices to indices
v_map = {v: i for i, v in enumerate(vertices)}

# Create adjacency matrix
n = len(vertices)
matrix = [[0 for _ in range(n)] for _ in range(n)]

# Filling matrix (Undirected Graph)
for start, end in edges:
    row, col = v_map[start], v_map[end]
    matrix[row][col] = 1
    matrix[col][row] = 1

# Printing matrix
print("   A  B  C  D")
print("----------------")
for i, row in enumerate(matrix):
    print(f"{vertices[i]} | {row}")

# Mapping degree of each vertex
degree = {}
for i in range(n):
    degree[vertices[i]] = sum(matrix[i])

# Printing degrees
print("\nDegrees of vertices:")
for v in vertices:
    print(f"deg({v}) = {degree[v]}")

# Verifying Handshaking Lemma
total_degree = sum(degree.values())
num_edges = len(edges)

print("\nVerification:")
print(f"Sum of degrees = {total_degree}")
print(f"2 × number of edges = {2 * num_edges}")

if total_degree == 2 * num_edges:
    print("Handshaking Lemma Verified")
else:
    print("Handshaking Lemma Not Verified")