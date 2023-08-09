
def main():
    print("Hello World")




if __name__ == "__main__":
    M, E, N, C = input().split(" ")
    # M = SALAS
    # E = CORREDORES
    # N = DUTOS
    # C = CONSULTAS 

    cons = input().split(" ")
    vent = input().split(" ")
    encounters = []

    for _ in range(C):
        encounters.append(input())