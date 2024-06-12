import time
from search_functions.dynamic_programming import dynamic_programming
from search_functions.brute_force import brute_force

def main():
    file_path = "items.txt"
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    C = int(lines[0].strip())
    n = int(lines[1].strip())
    items = []
    for line in lines[2:]:
        value, volume, name = line.split(";")
        items.append((int(value.strip()), int(volume.strip()), name.strip()))
    
    # Mierzenie czasu wykonania algorytmu programowania dynamicznego
    start_time = time.time()
    dp_max_value, dp_selected_items = dynamic_programming(C, items)
    dp_time = time.time() - start_time
    
    # Mierzenie czasu wykonania algorytmu brute force
    start_time = time.time()
    bf_max_value, bf_selected_items = brute_force(C, items)
    bf_time = time.time() - start_time
    
    print("Dynamic Programming:\n")
    print("Max Value:", dp_max_value)
    print("Selected Items:", dp_selected_items)
    print(f"\nExecution Time: {dp_time:.6f} seconds")
    
    print("\nBrute Force:\n")
    print("Max Value:", bf_max_value)
    print("Selected Items:", bf_selected_items)
    print(f"\nExecution Time: {bf_time:.6f} seconds")

if __name__ == "__main__":
    main()