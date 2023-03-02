import numpy as np
import random

def tsp(distances, iterations=1000):
    n = len(distances)
    current_solution = list(range(n))
    current_distance = calculate_distance(current_solution, distances)
    
    for i in range(iterations):
        neighbor = get_neighbor(current_solution)
        neighbor_distance = calculate_distance(neighbor, distances)
        
        if neighbor_distance < current_distance:
            current_solution = neighbor
            current_distance = neighbor_distance
    
    return current_distance

def calculate_distance(solution, distances):
    distance = 0
    for i in range(len(solution)):
        distance += distances[solution[i]][solution[(i+1)%len(solution)]]
    return distance

def get_neighbor(solution):
    i, j = random.sample(range(len(solution)), 2)
    neighbor = solution.copy()
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

distances = np.array([[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])
print(tsp(distances))
