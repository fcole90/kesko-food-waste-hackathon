import time

import numpy as np

from optimisation.utils import get_items_opt_cost, get_market_coordinates, get_items_expiring_soon, \
    get_geodesic_distance


def crossover(parent_a, parent_b):
    parent_a = parent_a.copy()
    parent_b = parent_b.copy()
    cross_index = np.random.randint(0, len(parent_a))
    offspring_a = [parent_a[i] for i in range(0, cross_index)] if cross_index > 0 else list()
    offspring_b = [parent_b[i] for i in range(0, cross_index)] if cross_index > 0 else list()

    for i in range(cross_index, len(parent_a)):
        if len(offspring_b) > 0 and parent_a[i] in offspring_b:
            offspring_a.append(parent_a[i])
            offspring_b.append(parent_b[i])
        else:
            offspring_a.append(parent_b[i])
            offspring_b.append(parent_a[i])
    return offspring_a, offspring_b


def mutation(gene, market_list, mutation_p=0.9):
    gene = gene.copy()
    for i in range(np.random.randint(0, 15)):
        mutation_factor_swap = np.random.rand()
        if mutation_factor_swap < mutation_p:
            a, b = np.random.randint(0, len(gene), size=2)
            gene[a], gene[b] = gene[b], gene[a]

        mutation_factor_hop = np.random.rand()
        if mutation_factor_hop < mutation_p:
            a, b = np.random.randint(0, len(gene)), np.random.randint(0, len(market_list))
            gene[a] = market_list[b]
    return gene


def get_best_ranked_markets(market_list,
                            items_list,
                            user_position,
                            distance_weight,
                            completeness_weight,
                            threshold_cost=None,
                            max_iterations=100,
                            max_survival_probability=0.9,
                            max_ranked_elements=10,
                            population_max_size=6,
                            retain_parents=True,
                            max_time=None):
    # Initial population
    if threshold_cost is None:
        threshold_cost = -np.inf
    if max_time is None:
        max_time = np.inf

    start_time = time.time()
    population_cost_list = None
    population = [np.random.choice(market_list, size=max_ranked_elements) for _ in range(population_max_size)]

    def market_cost_function(market):
        distance_objective = get_geodesic_distance(*user_position, *get_market_coordinates(market))
        completeness_objective = get_items_opt_cost(market, items_list)
        return (distance_objective * distance_weight)**2 * (completeness_weight * completeness_objective)**2

    def gene_cost_function(gene):
        gene_costs_list = [market_cost_function(market) for market in gene]
        cost = np.sum(gene_costs_list)
        original_cost = cost

        for i in range(0, len(gene_costs_list) - 1):
            if gene_costs_list[i] < gene_costs_list[i+1]:
                cost -= 0.01 * original_cost

        return cost


    for i in range(max_iterations):
        population_cost_list = [gene_cost_function(gene) for gene in population]
        population_max = np.max(population_cost_list)

        # for p in population:
        #     print([m["market_index"] for m in p])

        survival_probabilities = (1 - (np.array(population_cost_list) / population_max - 0.001)) * max_survival_probability
        # print("survival_probabilities:", survival_probabilities)
        survival_probabilities /= np.sum(survival_probabilities)
        # print("survival_probabilities:", survival_probabilities)

        if np.isnan(survival_probabilities).any():
            print("survival_probabilities:", survival_probabilities)
            print("population_cost_list:", population_cost_list)
            print("population_max:", population_max)
            print("max_survival_probability:", max_survival_probability)

        if np.isnan(survival_probabilities).any():
            parent_a_index, parent_b_index = np.random.choice(range(len(population)), size=2)
        else:
            parent_a_index, parent_b_index = np.random.choice(range(len(population)), size=2, p=survival_probabilities)

        parent_a, parent_b = population[parent_a_index], population[parent_b_index]
        offspring_a, offspring_b = crossover(parent_a, parent_b)

        offspring_size = min(len(population), population_max_size)
        offspring_a_size = offspring_size // 2
        offspring_b_size = offspring_size - offspring_a_size

        if retain_parents is True:
            offspring_a_size -= 1
            offspring_b_size -= 1

        offspring_a_list = [mutation(offspring_a, market_list) for _ in range(offspring_a_size - 1)] + [offspring_a]
        offspring_b_list = [mutation(offspring_b, market_list) for _ in range(offspring_b_size - 1)] + [offspring_b]

        if retain_parents is True:
            population = [parent_a, parent_b] + offspring_a_list + offspring_b_list
        else:
            population = offspring_a_list + offspring_b_list

        print(f"Iteration {i+1}, agv:{np.mean(population_cost_list)}, min:{np.min(population_cost_list)} -", [(population_cost_list[j]) for j in range(len(population))])

        if np.min(population_cost_list) < threshold_cost:
            break

        if time.time() - start_time > max_time:
            break

    best_population_ranking = population[np.argmax(population_cost_list)]
    best_population_cost_list = np.array([market_cost_function(market) for market in best_population_ranking])
    best_population_cost_list = best_population_cost_list.tolist()

    for i, market in enumerate(best_population_ranking):
        market["distance"] = float(get_geodesic_distance(*user_position, *get_market_coordinates(market)))
        market["completeness_cost"] = float(get_items_opt_cost(market, items_list))
        market["multiobjective_cost"] = best_population_cost_list[i]
        market["needed_on_expiry"] = [it for it in items_list if it in get_items_expiring_soon(market)]
        market["completeness_percentage"] = float(len(market["needed_on_expiry"]) / len(items_list)) * 100

    return sorted(best_population_ranking, key=lambda market: market["multiobjective_cost"]),\
           sorted(best_population_cost_list)
