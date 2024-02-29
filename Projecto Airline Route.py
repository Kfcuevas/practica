import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dest, cost):
        if src not in self.graph:
            self.graph[src] = []
        self.graph[src].append((dest, cost))

    def dijkstra(self, src, dest):
        pq = [(0, src, [])]  #queue de prioridad: (costo, Ciudad Actual, camino(ruta))
        visited = set()

        while pq:
            cost, node, path = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)
            path = path + [node]

            if node == dest:
                return path, cost

            if node not in self.graph:
                continue

            for neighbor, edge_cost in self.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + edge_cost, neighbor, path))

        return None, float('inf')

def find_optimal_route(cities, flight_costs, origin, destination):
    graph = Graph()

    for src, dest, cost in flight_costs:
        graph.add_edge(src, dest, cost)
        graph.add_edge(dest, src, cost)  # Vuelos bidireccionales

    route, total_cost = graph.dijkstra(origin, destination)

    if route:
        return route, total_cost
    else:
        return "Ruta no se encontro", -1

# Sample Input 1
cities1 = ["new york", "london", "paris", "tokyo", "dubai", "los angeles"]
flight_costs1 = [("new york", "london", 250), ("london", "paris", 100), ("paris", "tokyo", 500),
                 ("tokyo", "dubai", 300), ("dubai", "los angeles", 450), ("new york", "dubai", 600),
                 ("paris", "los angeles", 550)]
#origin1 = "New York"
#destination1 = "Los Angeles"

# Sample Input 2
cities2 = ["berlin", "moscow", "istanbul", "beijing", "mumbai", "cape town"]
flight_costs2 = [("berlin", "moscow", 180), ("moscow", "istanbul", 150), ("istanbul", "beijing", 350),
                 ("beijing", "mumbai", 400), ("mumbai", "cape town", 550), ("berlin", "istanbul", 220),
                 ("istanbul", "cape town", 500)]
#origin2 = "Berlin"
#destination2 = "Cape Town"


# iteramos para una confirmacion de la ciudad si esta en la lista
def get_city(prompt, cities):

    while True:
        city = input(prompt).strip().lower()
        if city in cities:
            return city
        else:
            print('La ciudad no es valida!')

# Aqui probamos si el mecanismo funciona con los ejemplos de las ciudades dadas en le sample #1
# creamos funciones para manejar un menu pricipal
def city1flightcaculator():
    while True:
        try:
            print('''Sistema de verificacion de costo efectividad de vuelos por sus rutas.''')
            respuesta = input("Desea Comenzar con la prueba? ('s' o 'n'): ").lower()

            if respuesta.startswith ('s'):# si la respuesta empieza con la letra s
                print("Aqui una lista de ciudades disponibles:")
                # imprimiendo las ciudades para el usuario
                for l in cities1:
                    print(f'{l}')
                origin1 = get_city('Introdice la ciudad de origen: ', cities1)
                destination1 = get_city('Introduce la ciudad destino: ', cities1)

                print(f'Origen: {origin1} y destino: {destination1}')
                print(f'Las rutas obtimas y sus costostotal: ', find_optimal_route(cities1, flight_costs1, origin1, destination1))


            elif respuesta.startswith('no'):# si la respuesta empieza con la letra n
                confrm2 = input("Eligio 'no', Salir del programa? ('s' o 'n')").lower()
                if confrm2.startswith('s'):
                    print('Gracias por usasr el programa!')
                    break
                elif confrm2.startswith('n'):
                    print("Regresando al menu principal!")
                    
                else:
                    print("Respuesta erronea introduzca ('s' o 'n')")

            else:
                print("Respuesta no válida. Por favor, introduzca 's' o 'n'.")

        except ValueError:
            print('Por favor introduzca valores correctos')

# Aqui probamos si el mecanismo funciona con los ejemplos de las ciudades dadas en le sample #2
# creamos funciones para manejar un menu pricipal
def city2flightcaculator():
    while True:
        try:
            print('''Sistema de verificacion de costo efectividad de vuelos por sus rutas.''')
            respuesta = input("Desea Comenzar con la prueba? ('s' o 'n'): ").lower()

            if respuesta.startswith ('s'):# si la respuesta empieza con la letra s
                print("Aqui una lista de ciudades disponibles:")
                # imprimiendo las ciudades para el usuario
                for l in cities2:
                    print(f'{l}')
                origin2 = get_city('Introdice la ciudad de origen: ', cities2)
                destination2 = get_city('Introduce la ciudad destino: ', cities2)

                print(f'Origen: {origin2} y destino: {destination2}')
                print(f'Las rutas obtimas y sus costostotal: ', find_optimal_route(cities2, flight_costs2, origin2, destination2))


            elif respuesta.startswith('no'):# si la respuesta empieza con la letra n
                confrm2 = input("Eligio 'no', Salir del programa? ('s' o 'n')").lower()
                if confrm2.startswith('s'):
                    print('Gracias por usasr el programa!')
                    break
                elif confrm2.startswith('n'):
                    print("Regresando al menu principal!")
                    
                else:
                    print("Respuesta erronea introduzca ('s' o 'n')")

            else:
                print("Respuesta no válida. Por favor, introduzca 's' o 'n'.")

        except ValueError:
            print('Por favor introduzca valores correctos')


# Main menu
while True:
    print('''
Bienvenido a Caribean Peseteros Flight

Seleccione segun su destino:
        Opcion# 1. Vuelos y destinos disponibles ("new york", "london", "paris", "tokyo", "dubai", "los angeles")
        Opcion# 2. Vuelos y destinos disponibles ("berlin", "moscow", "istanbul", "beijing", "mumbai", "cape town")
''')

    respuestamenu = int(input("Entre numero del menu deseado: "))

    if respuestamenu == int(1):
        city1flightcaculator()

    elif respuestamenu == int(2):
        city2flightcaculator()
    else:
        print("respuesta invalida")