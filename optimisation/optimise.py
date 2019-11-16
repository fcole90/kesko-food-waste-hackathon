import numpy as np

from optimisation.utils import get_distance, get_items_opt_cost, get_market_coordinates


def crossover(parent_a, parent_b):
    cross_index = np.random.randint(0, len(parent_a))
    offspring_a = parent_a[0: cross_index]
    offspring_b = parent_b[0: cross_index]

    for i in range(cross_index, len(parent_a)):
        if parent_a[i] in offspring_b:
            offspring_a.append(parent_a[i])
            offspring_b.append(parent_b[i])
        else:
            offspring_a.append(parent_b[i])
            offspring_b.append(parent_a[i])
    return offspring_a, offspring_b


def mutation(gene, mutation_p=0.9):
    for i in range(np.random.randint(0, 3)):
        mutation_factor = np.random.rand()
        a, b = np.random.randint(0, len(gene), size=2)
        if mutation_factor > mutation_p:
            gene[a], gene[b] = gene[b], gene[a]
    return gene


def get_best_ranked_markets(market_list,
                            items_list,
                            user_position,
                            distance_weight,
                            completeness_weight,
                            threshold_cost=None,
                            max_iterations=100,
                            max_survival_probability=0.9,
                            offspring_max_size=6,
                            retain_parents=True):
    # Initial population
    population_cost_list = None
    population = market_list

    def cost_function(market):
        distance_objective = get_distance(*user_position, *get_market_coordinates(market))
        completeness_objective = get_items_opt_cost(market, items_list)
        return (distance_objective * distance_weight)**2 * (completeness_weight * completeness_objective)**2

    for i in range(max_iterations):
        population_cost_list = [cost_function(market) for market in population]
        population_max = np.max(population_cost_list)

        if np.min(population_cost_list) < threshold_cost:
            break

        survival_probabilities = max_survival_probability - (np.array(population_cost_list) / population_max)

        parent_a, parent_b = np.random.choice(population, size=2, p=survival_probabilities)
        offspring_a, offspring_b = crossover(parent_a, parent_b)

        offspring_size = min(len(population), offspring_max_size)
        offspring_a_size = offspring_size // 2
        offspring_b_size = offspring_size - offspring_a_size

        if retain_parents is True:
            offspring_a_size -= 1
            offspring_b_size -= 1

        offspring_a_list = [mutation(offspring_a) for _ in range(offspring_a_size - 1)] + [offspring_a]
        offspring_b_list = [mutation(offspring_b) for _ in range(offspring_b_size - 1)] + [offspring_b]

        if retain_parents is True:
            population = [parent_a, parent_b] + offspring_a_list + offspring_b_list
        else:
            population = offspring_a_list + offspring_b_list

    for i, market in enumerate(population):
        market["distance"] = float(get_distance(*user_position, *market["location"]))
        market["completeness_cost"] = float(get_items_opt_cost(market, items_list))
        market["multiobjective_cost"] = float(population_cost_list[i])

    return np.sort(population, order="multiobjective_cost")
