import sys
import math

def create_adjacency_list(filename):
    adjacency_list = {}
    with open(filename, 'r') as file:
        for line in file:
            city1, city2 = map(int, line.strip().split())
            if city1 not in adjacency_list:
                adjacency_list[city1] = []
            if city2 not in adjacency_list:
                adjacency_list[city2] = []
            adjacency_list[city1].append(city2)
            adjacency_list[city2].append(city1)
    return adjacency_list

def generate_grid_graph(x, y):
    adjacency_list = {}
    for row in range(y):
        for col in range(x):
            node = row * x + col
            if node not in adjacency_list:
                adjacency_list[node] = []
            
            if col < x - 1:
                right_node = node + 1
                adjacency_list[node].append(right_node)
                if right_node not in adjacency_list:
                    adjacency_list[right_node] = []
                adjacency_list[right_node].append(node)
            
            if row < y - 1:
                bottom_node = node + x
                adjacency_list[node].append(bottom_node)
                if bottom_node not in adjacency_list:
                    adjacency_list[bottom_node] = []
                adjacency_list[bottom_node].append(node)
                
    return adjacency_list

def select_cities_for_charging_stations(connectivity_list):
    covered = set()
    stations = set()

    while len(covered) < len(connectivity_list):
        max_cover = 0
        best_cities = []
        for city, neighbors in connectivity_list.items():
            # Calculate the cover as the number of uncovered neighbors
            cover = sum(1 for neighbor in neighbors if neighbor not in covered) + (city not in covered)
            # If this city covers more than the current max, it becomes the new best city
            if cover > max_cover:
                max_cover = cover
                best_cities = [city]
            elif cover == max_cover:
                best_cities.append(city)
        
        # Tie-breaking among the best cities
        if len(best_cities) > 1:
            min_connections = float('inf')
            for city in best_cities:
                # Count total connections for the city and its direct neighbors
                connections = sum(len(connectivity_list[neighbor]) for neighbor in connectivity_list[city])
                if connections < min_connections:
                    min_connections = connections
                    best_city = city
        else:
            best_city = best_cities[0]

        covered.add(best_city)
        stations.add(best_city)
        for neighbor in connectivity_list[best_city]:
            covered.add(neighbor)

    return sorted(stations), len(stations)


if __name__ == "__main__":
    flag = sys.argv[1]

    if flag == '1':
        filename = sys.argv[2]
        adjacency_list = create_adjacency_list(filename)
        print(adjacency_list)
        stations, count = select_cities_for_charging_stations(adjacency_list)
        print(stations, count)

    elif flag == '2':
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        optimal_stations = generate_grid_graph(x, y)
        stations, count = select_cities_for_charging_stations(optimal_stations)

        print("Optimálny počet: " + str(count) + " ... " + str(stations))

        aprx = 0
        if (x == 4 and y >= 10): 
            aprx = y
        elif (x == 6 and y >= 7): 
            aprx = math.ceil((10*y + 4) / 7)
        else: aprx = math.ceil(((x+2) * (y+2)) / 5 - 4)

        print("Pomer: " + str(count / aprx))
    else:
        print("Invalid flag. Please use 'task1' or 'task2'.")