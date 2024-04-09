def load_tsp_data(file_path):
    coordinates = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line[0].isnumeric():
                parts = line.split()
                node_number = int(parts[0])
                x, y = float(parts[1]), float(parts[2])
                coordinates[node_number] = (x, y)
    return coordinates

file_path = 'data1.txt'
coordinates = load_tsp_data(file_path)
print(coordinates)

