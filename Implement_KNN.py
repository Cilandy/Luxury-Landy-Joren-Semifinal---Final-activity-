import math

def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def normalize(data):
    transposed = list(zip(*data))
    mins = [min(col) for col in transposed]
    maxs = [max(col) for col in transposed]
    return [
        [(x - min_val) / (max_val - min_val) if max_val != min_val else 0
         for x, min_val, max_val in zip(row, mins, maxs)]
        for row in data
    ]

def predict_knn(new_point, data, labels, k):
    distances = []
    for point, label in zip(data, labels):
        dist = euclidean_distance(new_point, point)
        distances.append((dist, label))

    distances.sort(key=lambda x: x[0])
    k_neighbors = distances[:k]

    votes = {}
    for _, label in k_neighbors:
        votes[label] = votes.get(label, 0) + 1

    return max(votes, key=votes.get)

# Example usage
data = [[1, 2], [2, 3], [3, 3], [6, 5]]
labels = ["A", "A", "A", "B"]
new_point = [2, 2]

print(predict_knn(new_point, data, labels, k=3))
