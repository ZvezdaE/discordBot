
'''
Layout for a tile
1  2  4
8  0  16
32 64 128

'''
def print_tile(tile_list):
    positions = [1,2,4,8,0,16,32,64,128]
    tile = []
    for x in positions:
        if x in tile_list:
            if x == 1:
                tile.append(" \\")
            if x == 2:
                tile.append("|")
            if x == 4:
                tile.append("/\n")
            if x == 8:
                tile.append("-")
            if x == 16:
                tile.append("-\n")
            if x == 32:
                tile.append("/")
            if x == 64:
                tile.append("|")
            if x == 128:
                tile.append("\\\n")
        else:
            if x == 4 or x == 16 or x == 128:
                tile.append("*\n")
            elif x == 1:
                tile.append(" *")
            else:
                tile.append("*")

    print(*tile)

    return tile

def decompose(x):
    divider = 128
    number_list = []
    while divider >= 1:
        if x % divider < x:
            number_list.insert(0,int(divider))
            x -= divider
        divider = divider / 2

    return number_list

def generate_map(seed: str, size: int):
    for x in range(size*size):
        print(x+1)

generate_map(1,5)