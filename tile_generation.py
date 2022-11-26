#------------------------------------------------------------------
# A set of classes to manage the tile generation for the map.
# The map is an expanding grid as the user navigates.
# Each tile is randomly generated when first encountered with
# the settings influenced by the surrounding tiles
# 
# ----------------------------------------------------------------- 

import random

'''
A class to manage the location(point) on the grid
'''    
class point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        """Create a point object with the provided credentials."""
        self.__x = x
        self.__y = y

    def __hash__(self):
        """Create a hash value of the object, use in dictionaries."""
        return hash((self.__x, self.__y))

    def __eq__(self, comp_point):
        """Check if 2 points are equal to each other."""
        return (self.__x, self.__y) == (comp_point.__x, comp_point.__y)

    def __ne__(self, comp_point):
        """Check if 2 points are not equal to each other"""
        return not(self == comp_point)

    def get_x(self):
        """Return the x coordinate of the point."""
        return self.__x

    def get_y(self):
        """Returns the y coordinate of the point."""
        return self.__y

    def set_x(self, x: int):
        """Make a change to the x value of the point."""
        self.__x = x
    
    def set_y(self, y: int):
        """Make a change to the y value of the point"""
        self.__y = y

    def __str__(self):
        """Define how the point will be displayed using the Print function"""
        return "[" + str(self.get_x()) + "," + str(self.get_y()) + "]"

    def __add__(self, other_point):
        """Add x and y values to the point"""
        other_point.__x = self.__x + other_point.__x
        other_point.__y = self.__y + other_point.__y

        return other_point

    def __sub__(self, other_point):
        """Subtract x and y values from the point"""
        other_point.__x = self.__x - other_point.__x
        other_point.__y = self.__y - other_point.__y

        return other_point

    def move(self, x: int = 0, y: int = 0):
        self.__x += x
        self.__y += y


'''
A class to create and manage the details of tile elements
'''
class tile_element:
    def __init__(self, path_list = [0,0,0,0], enviro_list = [0,0,0]):
        """Create a new tile object."""
        if random.random() > 0.97:
            self.town = 1
        else:
            self.town = 0
        
        __grass_value = (1 + enviro_list[0]) ** enviro_list[0]
        __forest_value = (1 + enviro_list[1]) ** enviro_list[1]
        __mount_value = (1 + enviro_list[2]) ** enviro_list[2]
        __total_env = __grass_value + __forest_value + __mount_value
        __environ_rand = random.random()
        if __environ_rand < __grass_value/__total_env:
            self.environ = 0
        elif __environ_rand > __mount_value/__total_env:
            self.environ = 2
        else:
            self.environ = 1
        __key = random.randint(1,8)
        self.paths = self.__decompose(__key)
        if path_list[0] == 1:
            if not 1 in self.paths:
                self.paths.append(1)
        elif path_list[0] == -1:
            if 1 in self.paths:
                self.paths.remove(1)
        if path_list[1] == 1:
            if not 2 in self.paths:
                self.paths.append(2)
        elif path_list[1] == -1:
            if 2 in self.paths:
                self.paths.remove(2)
        if path_list[2] == 1:
            if not 4 in self.paths:
                self.paths.append(4)
        elif path_list[2] == -1:
            if 4 in self.paths:
                self.paths.remove(4)
        if path_list[3] == 1:
            if not 8 in self.paths:
                self.paths.append(8)
        elif path_list[3] == -1:
            if 8 in self.paths:
                self.paths.remove(8)

    
    def __decompose(self, x):
        """Create and return a list of the 2^n values that make up x."""
        __divider = 8
        __number_list = []
        while __divider >= 1:
            if x % __divider < x:
                __number_list.insert(0,int(__divider))
                x -= __divider
            __divider = __divider / 2
        return __number_list

    def get_environ(self):
        """Return the int value of the environment type"""
        return self.environ

    def get_environ_desc(self):
        """Provide a text description of the tile environment"""
        if self.environ == 0:
            return "you are standing on a grassy plain."
        if self.environ == 1:
            return "you are standing in a dark forest."
        if self.environ == 2:
            return "you are standing amoung mighty mountains."

    def get_town(self):
        """Return the text description for the town value"""
        if self.town == 1:
            return "You see a small town in the distance."
        else:
            return ""

    def get_paths(self):
        """Return the list of paths for the tile."""
        return self.paths
    
    def get_paths_text(self):
        """Return the text description of the paths for the tile."""
        __path_count = len(self.paths)
        if __path_count == 1:
            __sen_start = "There is a path heading to the "
        else:
            __sen_start = "There are paths heading to the "
        __first_direct = self.__path_direct(self.paths[0])
        if __path_count > 1:
            __second_direct = self.__path_direct(self.paths[1])
        if __path_count > 2:
            __third_direct = self.__path_direct(self.paths[2])
        if __path_count > 3:
            __fourth_direct = self.__path_direct(self.paths[3])
        
        if __path_count == 1:
            return __sen_start + __first_direct + "."
        if __path_count == 2:
            return __sen_start + __first_direct + " and " + __second_direct + "."
        if __path_count == 3:
            return __sen_start + __first_direct + ", " + __second_direct + " and " + __third_direct + "."
        if __path_count == 4:
            return __sen_start + __first_direct + ", " + __second_direct + ", " + __third_direct + " and " + __fourth_direct + "."

    def __path_direct(self, direct):
        """Transform the path int into text."""
        if direct == 1:
            return "North"
        if direct == 2:
            return "West"
        if direct == 4:
            return "East"
        if direct == 8:
            return "South"

    def tile_description(self):
        """Return the full description of the tile."""
        __enviro = self.get_environ_desc()
        __paths = self.get_paths_text()
        __town = self.get_town()
        
        return "> " + __enviro + "\n" + __paths + "\n" + __town


"""
A class to create and update the map using a dictionary
"""

class map:
    def __init__(self): 
        """Initiate the map object with starting point and tile."""
        __initial_point = point(0,0)
        self.map_dict = {__initial_point : tile_element()}

    def get_tile(self, tile_loc):
        """Return the details of the requested tile."""
        if tile_loc in self.map_dict:
            return self.map_dict[tile_loc]

    def add_tile(self, tile_loc, path_list=[0,0,0,0], envion_list = [0,0,0]):
        """Add a new tile to the map."""
        print(f'Path list: {path_list}')
        print(f'Environ list: {envion_list}')
        self.map_dict[tile_loc] = tile_element(path_list, envion_list)
    
    def check_tile(self, tile_loc):
        """Check to see if the supplied point is in the dictionary."""
        return tile_loc in self.map_dict

    def __check_enviro(self, tile_loc, check_list):
        """Increment a position in a list depending on environment int value."""
        __temp_env = self.get_tile(tile_loc).get_environ()
        if __temp_env == 0:
            check_list[0] += 1
        elif __temp_env == 1:
            check_list[1] += 1
        elif __temp_env == 2:
            check_list[2] += 1

        return check_list

    def get_surround(self, tile_loc):
        """Return lists listing the surround paths leading into the tile and the surrounding environments."""
        __leading_paths = []
        __surrounding_enviro = [0,0,0]
        __temp_loc = tile_loc + point(0,1)
        if self.check_tile(__temp_loc):
            __temp_tile = self.get_tile(__temp_loc)
            __surrounding_enviro = self.__check_enviro(__temp_loc, __surrounding_enviro)
            if 8 in __temp_tile.get_paths():
                __leading_paths.append(1)
            else:
                __leading_paths.append(-1)
        else: 
            __leading_paths.append(0)
        
        __temp_loc = tile_loc + point(-1,0)
        if self.check_tile(__temp_loc):
            __temp_tile = self.get_tile(__temp_loc)
            __surrounding_enviro = self.__check_enviro(__temp_loc, __surrounding_enviro)
            if 4 in __temp_tile.get_paths():
                __leading_paths.append(1)
            else:
                __leading_paths.append(-1)
        else:
            __leading_paths.append(0)

        if self.check_tile(tile_loc + point(1,0)):
            __temp_tile = self.get_tile(tile_loc + point(1,0))
            __surrounding_enviro = self.__check_enviro(tile_loc + point(1,0), __surrounding_enviro)
            if 2 in __temp_tile.get_paths():
                __leading_paths.append(1)
            else:
                __leading_paths.append(-1)
        else: 
            __leading_paths.append(0)

        if self.check_tile(tile_loc + point(0,-1)):
            __temp_tile = self.get_tile(tile_loc + point(0,-1))
            __surrounding_enviro = self.__check_enviro(tile_loc + point(0,-1), __surrounding_enviro)
            if 1 in __temp_tile.get_paths():
                __leading_paths.append(1)
            else:
                __leading_paths.append(-1)
        else:
            __leading_paths.append(0)

        return __leading_paths, __surrounding_enviro

class character:
    def __init__(self):
        """Inititalise the character and associated map."""
        self.my_map = map()
        self.location = point(0,0)
        #self.name = name

    def move(self, direction):
        """Move the character to another tile, if there is a path in that direction."""
        if direction == "N":
            if 1 in self.my_map.get_tile(self.location).get_paths():
                self.location = self.location + point(0,1)
                if self.my_map.check_tile(self.location):
                    return self.my_map.get_tile(self.location).tile_description()
                else:
                    __path_list, __enviro_list = self.my_map.get_surround(self.location)
                    self.my_map.add_tile(self.location, __path_list, __enviro_list)
                    return self.my_map.get_tile(self.location).tile_description()
            else:
                return "There is no path in that direction\n\n" + self.my_map.get_tile(self.location).tile_description()
        if direction == "S":
            if 8 in self.my_map.get_tile(self.location).get_paths():
                self.location = self.location + point(0,-1)
                if self.my_map.check_tile(self.location):
                    return self.my_map.get_tile(self.location).tile_description()
                else:
                    __path_list, __enviro_list = self.my_map.get_surround(self.location)
                    self.my_map.add_tile(self.location, __path_list, __enviro_list)
                    return self.my_map.get_tile(self.location).tile_description()
            else:
                return "There is no path in that direction\n\n" + self.my_map.get_tile(self.location).tile_description()
        if direction == "E":
            if 4 in self.my_map.get_tile(self.location).get_paths():
                self.location = self.location + point(1,0)
                if self.my_map.check_tile(self.location):
                    return self.my_map.get_tile(self.location).tile_description()
                else:
                    __path_list, __enviro_list = self.my_map.get_surround(self.location)
                    self.my_map.add_tile(self.location, __path_list, __enviro_list)
                    return self.my_map.get_tile(self.location).tile_description()
            else:
                return "There is no path in that direction\n\n" + self.my_map.get_tile(self.location).tile_description()
        if direction == "W":
            if 2 in self.my_map.get_tile(self.location).get_paths():
                self.location = self.location + point(-1,0)
                if self.my_map.check_tile(self.location):
                    return self.my_map.get_tile(self.location).tile_description()
                else:
                    __path_list, __enviro_list = self.my_map.get_surround(self.location)
                    self.my_map.add_tile(self.location, __path_list, __enviro_list)
                    return self.my_map.get_tile(self.location).tile_description()
            else:
                return "There is no path in that direction\n\n" + self.my_map.get_tile(self.location).tile_description()
    
    def new_map(self):
        self.my_map = map()
        self.location = point(0,0)
    
    def loc_desc(self):
        """Return the text description of the tile."""
        return self.my_map.get_tile(self.location).tile_description()

class inventory:
    def __init__(self):
        self.size = 6
        self.items = []
        self.full = False

    def add(self, item):
        if not self.full:
            self.items.append(item)
        if len(self.items) < 6:
            self.full = False

    def remove(self, item):
        for x in self.items:
            if x == item:
                self.item.remove(item)

class items:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.depends = []

    def add_depends(self, item):
        self.depends.append(item)