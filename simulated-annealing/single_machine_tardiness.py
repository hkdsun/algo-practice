import random
import math

processing_times = {
    1: 9,
    2: 9,
    3: 12,
    4: 3
}

due_times = {
    1: 10,
    2: 8,
    3: 5,
    4: 28
}

weights = {
    1: 14,
    2: 12,
    3: 1,
    4: 12
}

def reduce_temperature(temp):
    return 0.99 * temp

def random_order(arr):
    new_arr = list(arr)
    random.shuffle(new_arr)
    return new_arr

def accept_solution(delta, temperature):
    return random.random() < math.exp(-float(delta)/temperature)

def cost(solution):
    sum = 0
    time = 0
    for i in solution:
        time += processing_times[i]
        sum += weights[i] * max(0, (time - due_times[i]))
    return sum

def optimal_schedule(jobs):
    solution = random_order(jobs)
    temperature = 10
    print solution
    while cost(solution) > 100 and temperature > 0.1:
        for i in range(0, 100):
            swap_l = random.randint(0, len(solution)-1)
            swap_r = random.randint(0, len(solution)-1)
            while swap_r == swap_l:
                swap_r = random.randint(0, len(solution)-1)

            new_sol = list(solution)
            new_sol_r = solution[swap_l]
            new_sol_l = solution[swap_r]
            new_sol[swap_l] = new_sol_l
            new_sol[swap_r] = new_sol_r

            delta_cost = cost(new_sol) - cost(solution)
            if delta_cost < 0:
                solution = new_sol
                print solution, cost(solution), temperature
            else:
                if accept_solution(delta_cost, temperature):
                    solution = new_sol
                    print solution, cost(solution), temperature
        temperature = reduce_temperature(temperature)
    return solution

print optimal_schedule([1, 2, 3, 4])
