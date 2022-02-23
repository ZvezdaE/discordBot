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

    def __add__(self, x: int=0, y: int=0) -> None:
        """Add x and y values to the point"""
        self.__x += x
        self.__y += y

    def __sub__(self, x: int = 0, y: int = 0) -> None:
        """Subtract x and y values from the point"""
        self.__x -= x
        self._y -= y


'''
A class to create and manage the details of tile elements
'''
class tile_element:
    def __init__(self, loc, prev_town = 0, prev_env = 0):
        """Create a new tile object."""
        self.position = loc
        if random.random() > 0.97:
            self.town = 1
        else:
            self.town = 0
        
        self.environ = random.randint(0,2)
        __key = random.randint(1,15)
        self.paths = self.__decompose(__key)

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
        """Provide a text description of the tile environment"""
        if self.environ == 0:
            return "You are standing on a grassy plain."
        if self.environ == 1:
            return "You are standing in a dark forest."
        if self.environ == 2:
            return "You are standing amoung mighty mountains."

    def get_town(self):
        if self.town == 1:
            return "You see a small town in the distance."
        else:
            return ""

    def get_paths(self):
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
        if direct == 1:
            return "North"
        if direct == 2:
            return "West"
        if direct == 4:
            return "East"
        if direct == 8:
            return "South"

    def tile_description(self):
        __enviro = self.get_environ()
        __paths = self.get_paths()
        __town = self.get_town()
        
        return __enviro + "\n" + __paths + "\n" + __town


"""
A class to create and update the map using a dictionary
"""

class map:
    def __init__(self): 
        """Initiate the map object with starting point and tile."""
        __initial_point = point(0,0)
        self.map_dict = {__initial_point : tile_element(__initial_point)}

    def get_tile(self, tile_loc):
        """Return the details of the requested tile."""
        if tile_loc in self.map_dict:
            return self.map_dict[tile_loc]