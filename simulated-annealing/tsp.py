import random
import math

def dataset(filename):
    matrix = []
    with open(filename, 'r') as f:
        matrix = map(lambda x: map(lambda y: int(y), x.split()), f.readlines())
    return matrix

def reduce_temperature(temp):
    return 0.85 * temp

def random_order(arr):
    new_arr = list(arr)
    random.shuffle(new_arr)
    return new_arr

def accept_solution(delta, temperature):
    return random.random() < math.exp(-float(delta)/temperature)

def cost(solution, dataset):
    sum = 0
    for i in range(0, len(solution)-1):
        sum += dataset[solution[i]][solution[i+1]]
    sum += dataset[solution[len(solution)-1]][solution[0]]
    return sum

def optimal_schedule(cities, dataset):
    solution = random_order(cities)
    temperature = 10000
    while temperature > 0.1:
        for i in range(0, 8000):
            swap_l = random.randint(0, len(solution)-1)
            swap_r = random.randint(0, len(solution)-1)
            while swap_r == swap_l:
                swap_r = random.randint(0, len(solution)-1)

            new_sol = list(solution)
            new_sol_r = solution[swap_l]
            new_sol_l = solution[swap_r]
            new_sol[swap_l] = new_sol_l
            new_sol[swap_r] = new_sol_r

            delta_cost = cost(new_sol, dataset) - cost(solution, dataset)
            if delta_cost < 0:
                solution = new_sol
                print solution, cost(solution, dataset), temperature
            else:
                if accept_solution(delta_cost, temperature):
                    solution = new_sol
                    print solution, cost(solution, dataset), temperature
        temperature = reduce_temperature(temperature)
    return solution

data = dataset('berlin52.txt')
print optimal_schedule([x for x in range(0, len(data))], data)
