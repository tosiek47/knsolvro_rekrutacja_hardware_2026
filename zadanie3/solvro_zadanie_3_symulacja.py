import random
import math

packet_size = 64 # aby dobrze działał algorytm interleaving (przeplot) należy wprowadzić liczbę, której pierwiastek jest liczbą całkowitą ex. 64
simulation_runs = 10000

def simulate_random_errors(packet_size, error_probability = 0.05):
    return [1 if random.random() < error_probability else 0 for _ in range(packet_size)]
def simulate_burst_errors(packet_size, burst_length = 4):
    errors = [0] * packet_size
    starting_point = random.randint(0, packet_size - burst_length)
    for i in range (starting_point, starting_point + burst_length):
        errors[i] = 1
    return errors

def method_no_protection(errors):
    if sum(errors) == 0:
        return 1
    else:
        return 0

def method_hamming(errors, block_size = 8):
    for i in range(0, len(errors), block_size):
        block = errors[i:i + block_size]
        if sum(block) > 1:
            return 0
    return 1

def method_interleaving_hamming(errors, block_size = int(math.sqrt(packet_size))):
    interleaved_errors = []
    matrix_size = int(math.sqrt(packet_size))
    for i in range (matrix_size):
        for j in range(matrix_size):
            if (i + j * matrix_size) < len(errors):
                interleaved_errors.append(errors[i + j * matrix_size])
    return method_hamming(interleaved_errors, block_size)

def run_analysis():
    print("Analiza skuteczności protokołów dla " + str(simulation_runs) + " prób")
    print(f"{"Metoda ochrony":<25} | {"Skuteczność błędów losowych":<25} | {"Skuteczność błęów ciągłych"}")
    print("-" * 80)
    results = {
        "Brak ochrony": {"random": 0, "burst": 0},
        "Hamming (FEC)": {"random": 0, "burst": 0},
        "Przeplot + FEC": {"random": 0, "burst": 0}
    }

    for i in range(simulation_runs):
        random_error = simulate_random_errors(packet_size, 0.02)
        burst_error = simulate_burst_errors(packet_size, 4)

        if method_no_protection(random_error) : results["Brak ochrony"]["random"] += 1
        if method_no_protection(burst_error): results["Brak ochrony"]["burst"] += 1

        if method_hamming(random_error) : results["Hamming (FEC)"]["random"] += 1
        if method_hamming(burst_error): results["Hamming (FEC)"]["burst"] += 1

        if method_interleaving_hamming(random_error) : results["Przeplot + FEC"]["random"] += 1
        if method_interleaving_hamming(burst_error): results["Przeplot + FEC"]["burst"] += 1

    for method, scores in results.items():
        random_success = (scores["random"] / simulation_runs)
        burst_success = (scores["burst"] / simulation_runs)
        print(f"{method:<25} | {random_success:>27.1%} | {burst_success:>.1%}")

if __name__ == "__main__":
    run_analysis()
