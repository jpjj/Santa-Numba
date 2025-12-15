import numpy as np
from numpy.typing import NDArray


def save_christmas(
    route: NDArray[np.int_], distance_matrix: NDArray[np.float64]
) -> NDArray[np.int_]:
    """
    Function returning a 2-optimal solution to the tsp instance
    defined by distance_matrix. An improvement loop is run until
    no further improvement can be found.
    """
    improvement = True
    n = len(route)
    new_route = route.copy()
    while improvement:
        improvement = False
        for i in range(n):
            for j in range(i + 2, min(n + 1, i + n)):
                distance_diff = (
                    distance_matrix[new_route[i - 1]][new_route[i]]
                    + distance_matrix[new_route[j - 1]][new_route[j % n]]
                    - distance_matrix[new_route[i - 1]][new_route[j - 1]]
                    - distance_matrix[new_route[j % n]][new_route[i]]
                )

                if distance_diff > 0.001:
                    new_route[i:j] = new_route[i:j][::-1]
                    improvement = True
    return new_route
