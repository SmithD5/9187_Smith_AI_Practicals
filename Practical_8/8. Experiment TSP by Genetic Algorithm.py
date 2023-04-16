import numpy as np

# Create a distance matrix
# Distance between cities is represented by a 2D array
# where the element at the i-th row and j-th column represents the distance from city i to city j
# Note: The distance matrix should be symmetric (i.e., distance[i][j] == distance[j][i])
distance = np.array([
    [0, 30, 15, 20],
    [30, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

# Genetic Algorithm parameters
population_size = 50
num_generations = 100
mutation_rate = 0.1

# Function to calculate the total distance of a given route
def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Add distance from last city back to the starting city
    return total_distance

# Function to generate an initial population
def generate_initial_population(population_size, num_cities):
    population = []
    for _ in range(population_size):
        population.append(np.random.permutation(range(num_cities)))
    return population

# Function to perform crossover between two parent routes to generate two offspring routes
def crossover(parent1, parent2):
    cutoff = np.random.randint(0, len(parent1) - 1)  # Randomly select a cutoff point
    offspring1 = np.concatenate((parent1[:cutoff], np.setdiff1d(parent2, parent1[:cutoff])))
    offspring2 = np.concatenate((parent2[:cutoff], np.setdiff1d(parent1, parent2[:cutoff])))
    return offspring1, offspring2

# Function to perform mutation on a route
def mutate(route, mutation_rate):
    for i in range(len(route)):
        if np.random.rand() < mutation_rate:
            j = np.random.randint(0, len(route))
            route[i], route[j] = route[j], route[i]
    return route

# Main Genetic Algorithm function
def genetic_algorithm(distance_matrix, population_size, num_generations, mutation_rate):
    num_cities = distance_matrix.shape[0]
    population = generate_initial_population(population_size, num_cities)

    for generation in range(num_generations):
        # Calculate the fitness of each individual in the population
        fitness = [1 / calculate_total_distance(route, distance_matrix) for route in population]
        # Select the top 50% of individuals based on their fitness
        selected_indices = np.argsort(fitness)[-population_size//2:]
        selected_population = [population[i] for i in selected_indices]

        # Create a new population by crossover and mutation
        new_population = []
        while len(new_population) < population_size:
            parent1 = selected_population[np.random.randint(0, len(selected_population))]
            parent2 = selected_population[np.random.randint(0, len(selected_population))]
            offspring1, offspring2 = crossover(parent1, parent2)
            offspring1 = mutate(offspring1, mutation_rate)
            offspring2 = mutate(offspring2, mutation_rate)
            new_population.append(offspring1)
            new_population.append(offspring2)

        population = new_population

    # Find the best route in the final population
    best_route = min(population, key=lambda x: calculate_total_distance(x, distance_matrix))

    # Return the best route and its total distance
    return best_route, calculate_total_distance(best_route, distance_matrix)

# Run the Genetic Algorithm
best_route, total_distance = genetic_algorithm(distance, population_size, num_generations, mutation_rate)

# Print the best route and its total distance
print("Best route found:", best_route)
print("Total distance of best route:", total_distance)
