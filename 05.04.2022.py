map = [
    [12, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 24]
]

vaba_tee = 0
sein = 1

start_x = 0
start_y = 0
#2 1 praegused kordinaadid
def saab_liikuda_paremale(map, praegused_kordinaadid):
    y = praegused_kordinaadid[2]
    x = praegused_kordinaadid[1]
    print("Praegused kordinaadid")
    print(praegused_kordinaadid)
    print(map[y][x] == vaba_tee)
    print("parem")
    return False

def saab_liikuda_alla(map, praegused_kordinaadid):
    y = praegused_kordinaadid[1]
    x = praegused_kordinaadid[2]
    print("Praegused kordinaadid")
    print(praegused_kordinaadid)
    print(map[3][1] == vaba_tee)
    print("alla")
    return False

def saab_liikuda_vasakule(map, praegused_kordinaadid):
    y = praegused_kordinaadid[1]
    x = praegused_kordinaadid[0]
    print("Praegused kordinaadid")
    print(praegused_kordinaadid)
    print(map[2][0] == vaba_tee)
    print("vasak")
    return False

def saab_liikuda_ules(map, praegused_kordinaadid):
    y = praegused_kordinaadid[0]
    x = praegused_kordinaadid[1]
    print("Praegused kordinaadid")
    print(praegused_kordinaadid)
    print(map[1][0] == vaba_tee)
    print("ules")
    return False

def print_kaart():
    print(map[0])
    print(map[1])
    print(map[2])
    print(map[3])
    print(map[4])

print(saab_liikuda_paremale(map, [1, 1]))
print(saab_liikuda_alla(map, [1, 1]))
print(saab_liikuda_vasakule(map, [1, 1]))
print(saab_liikuda_ules(map, [1, 1]))

print_kaart()