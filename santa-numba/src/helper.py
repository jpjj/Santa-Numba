import numpy as np


def get_distance(route: np.array, distance_matrix: np.array) -> float:
    result = 0.0
    n = len(route)
    for i in range(len(route)):
        result += distance_matrix[route[i]][route[(i + 1) % n]]
    return result
