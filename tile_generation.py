import random
    
'''
manage the details of each tile element
'''
class tile_element:
    #initiate a new tile in the map
    def __init__(self, prev_town = 0, prev_env = 0, prev_path = 0):
        #self.position = [x,y]
        if random.random() > 0.95:
            self.town = 1
        else:
            self.town = 0
        
        self.environ = 1
        key = random.randint(1,15)
        paths = self.decompose(key)
        print(*paths)
        if prev_path != 0:
            if prev_path == 1:
                prev_path = 8
            elif prev_path == 8:
                prev_path = 1
            elif prev_path == 2:
                prev_path = 4
            elif prev_path == 4:
                prev_path = 2
            if prev_path not in paths:
                paths.append(prev_path)
                
        print(f'Key is {key}')
        if 1 in paths:
            self.N = 1
        else:
            self.N = None
        if 2 in paths:
            self.W = 1
        else:
            self.W = None
        if 4 in paths:
            self.E = 1
        else:
            self.E = None
        if 8 in paths:
            self.S = 1
        else:
            self.S = None

    def decompose(self, x):
        divider = 8
        number_list = []
        while divider >= 1:
            if x % divider < x:
                number_list.insert(0,int(divider))
                x -= divider
            divider = divider / 2
        return number_list


